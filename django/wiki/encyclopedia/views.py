from django.http import HttpResponse
from django.shortcuts import render
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
