from django.shortcuts import render
from markdown2 import Markdown



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
    
# Function call entry
def entry(request, title):
    html_content = md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry doesn't exits"
        })
    else:
        return render(request, "encyclopedia/entry.html")
