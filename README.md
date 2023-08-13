# Wiki
Design of Wikipedia-like online encyclopedia. Uses Github Markdown syntax to write the contents of encyclopedia.

For more details: https://cs50.harvard.edu/web/2020/projects/1/wiki/


## Deployment

you can see it here: https://wiki-vyr0.onrender.com

## What was used?

 - Django
 - Markdown2
 - HTML


## Youtube Video

This is a short video where you can see the project specifications: 

## Assignment specification
- **Entry Page**. Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
    - The view should get the content of the encyclopedia entry by calling the appropriate util function.
    - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
- **Index Page**. Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
- **Search**.  Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
    - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
    - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
    - Clicking on any of the entry names on the search results page should take the user to that entry’s page. 
- **New Page**. Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
    - Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
    - Users should be able to click a button to save their new page.
    - Users should be able to click a button to save their new page.
    - Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
- **Edit Page**. On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
    - The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
    - The user should be able to click a button to save the changes made to the entry.
    - Once the entry is saved, the user should be redirected back to that entry’s page.
- **Random Page**. Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

## Extra functionality

The delete function implements the ability to delete an encyclopedia entry. When a POST HTTP request is made, the function retrieves the title of the entry provided in the request. It then checks to see if a file associated with that title exists on the storage system. If the file exists, it is deleted and the user is redirected back to the index page.

         
### Built with:
--------------------

  1. [Bootstrap (version: 5)](https://getbootstrap.com/)

  2. [Microsoft Visual code (version:1.81.1)](https://code.visualstudio.com/)
    
  3. [Django version (version:3.2.20)](https://www.djangoproject.com/)
  
  6. [Jinja2 (version: 3.1)](https://jinja.palletsprojects.com/en/3.1.x/)
  
  7. [Python(version 3.11.1)](https://www.python.org/)
  
  8. HTML5

  10. Cascading Style Sheets (CSS)

--------------------

## Run Locally

Clone the project

```bash
  git clone https://github.com/Orrv2904/Project1-Wiki.git
```

Install dependencies

In case you want to use a virtual environment:

```bash
  python3 -m venv environment
  source environment/bin/activate
```

Install dependencies with pip

```bash
  pip install requirements.txt
```

Go to the project directory

```bash
  cd Project1-Wiki
```

runs the migrations

```bash
  python3 -m manage.py makemigrations
  python3 -m manage.py migrate
```

After that

```bash
  python3 -m manage.py runserver
```
    

## Authors

- [@orrv2904](https://github.com/Orrv2904)

