from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    
    fweb = markdown2.markdown(util.get_entry(title))

    return render(request, "encyclopedia/page.html", {
        "title": title is not None,
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