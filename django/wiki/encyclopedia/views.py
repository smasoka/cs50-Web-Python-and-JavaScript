from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import choice
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    
    fweb = markdown2.markdown(util.get_entry(title))

    return render(request, "encyclopedia/page.html", {
        "title": title if title is not None else "Not Found",
        "fweb": fweb if fweb is not None else "Not Found"
    })

def search(request):
    query = request.GET.get('q')
    
    if util.get_entry(query):
        return HttpResponseRedirect(reverse("page", args=(query,)))
    else:
        matched_list = []
        for entry in util.list_entries():
            if query in entry:
                matched_list.append(entry)
        
        return render(request, "encyclopedia/search.html", {
            "matched_list": matched_list
        })

def new_entry(request):
    if request.method == "POST":
        title = request.POST['title']
        entry_content = request.POST['entry-content']
        if title in util.list_entries():
            return HttpResponse("Entry already exists")
        
        filename = "entries/" + title + ".md"
        with open(filename, "w") as f:
            f.write(entry_content)
        
        return HttpResponseRedirect(reverse("page", args=(title,)))
    
    return render(request, "encyclopedia/new_entry.html")

def edit_page(request, title):
    if request.method == "POST":
        title = request.POST['title']
        entry_content = request.POST['entry-content']
        filename = "entries/" + title + ".md"
        with open(filename, "w") as f:
            f.write(entry_content)
        return HttpResponseRedirect(reverse("page", args=(title,)))

    entry_content = util.get_entry(title)
    if entry_content is None:
        return HttpResponseRedirect(reverse("index"))

    return render(request, "encyclopedia/edit_page.html", {
        "edit_title": title,
        "edit_content": entry_content
    })

def random_page(request):
    random_title = choice(util.list_entries())
    return HttpResponseRedirect(reverse("page", args=(random_title,)))