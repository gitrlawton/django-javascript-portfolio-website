from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here (views are what are used to display a page.  A view
# is something that will be called when you visit a route.)

# This view takes in a request...
def home(request):
    # ...and renders the request along with the home.html template.
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

# This view takes in a request and a project id...
def project(request, id):
    return render(request, "project.html")
