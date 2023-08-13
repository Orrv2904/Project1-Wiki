from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from markdown2 import Markdown
import random


from . import util

 # This view renders the index.html with a list of entries.
 # It uses the util.list_entries() function to retrieve the list of entries.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Convert Markdown content to HTML using the provided title.
# Returns None if no content found, otherwise returns HTML-converted content.
def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    
# Converts the Markdown content of the given title to HTML using md_to_html().
# Renders either an error page or the entry page based on availability.
def entry(request, title):
    html_content = md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry doesn't exits"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

# Handles the search functionality for encyclopedia entries.
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": entry_search,
                "content": html_content
                })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })

# Manages new encyclopedia page creation: renders creation form (GET),
# processes form data, checks title existence, and renders accordingly (POST).       
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "Entry page alredy exist"
            })
        else:
            util.save_entry(title, content)
            html_content = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })

# Renders the edit form with existing entry content for editing (POST).       
def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": content
        })

# Saves edited entry content (POST), updates entry, and renders entry page.    
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
            })
    
# Selects a random entry and renders its content as HTML.
# Returns a random encyclopedia entry page.
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html",{
        "title": rand_entry, 
        "content": html_content
    })

def delete(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        filename = f"entries/{title}.md"
        if default_storage.exists(filename):
            default_storage.delete(filename)
            return redirect('index')  # Redirige al índice después de la eliminación
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry not found"
            })