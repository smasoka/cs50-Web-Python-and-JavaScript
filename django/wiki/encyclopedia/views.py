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
    
    if title in util.list_entries():
        fweb = markdown2.markdown(util.get_entry(title))

        return render(request, "encyclopedia/page.html", {
            "title": title,
            "fweb": fweb
        })
    else:
        return HttpResponse("Entry not found!")

def search_results(request):
    if request.method == "POST":
        query = request.POST.get('q')
        if query in util.list_entries():
            return HttpResponseRedirect(reverse("page", query))
        else:
            query_list = []
            for entry in util.list_entries:
                if query in entry:
                    query_list.append(entry)
            return render(request, "encyclopedia/search_results", {
                "query_list": query_list
            })
