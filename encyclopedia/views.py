from django.shortcuts import render

from . import util


def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    coffe = util.get_entry("coffe")
    print(entries)
    print(css_file)
    print(coffe)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

