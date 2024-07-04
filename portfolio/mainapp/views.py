from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here (views are what are used to display a page.  A view
# is something that will be called when you visit a route.)

# This view takes in a request...
def home(request):
    # Collects all the different projects that exist.
    projects = Project.objects.all()
    # Collects all the different tags that exist.
    tags = Tag.objects.all()
    # ...and renders the request along with the home.html template, passing
    # the template a dictionary containing the projects and tags.  This gives
    # us access to the projects and tags variables from the home.html file.
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

# This view takes in a request and a project id...
def project(request, id):
    return render(request, "project.html")
