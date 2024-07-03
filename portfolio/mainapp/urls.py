# Note: This urls.py file was created manually by us.

from django.urls import path
from . import views

# List all the url paths.
urlpatterns = [
    # If we go to "", render the home view.
    path("", views.home, name="home"),
    # If we go to home/, also render the home view.
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    # Example: If we go to project/1/, render the project view for the project
    # with an id of 1.
    # To use a variable path, specify the variable type and name inside < >.
    path("project/<int:id>/", views.project, name="project"),
]

# Note: After listing the url paths, go to the main urls.py file which was
# created by Django, located in another folder (in this case, portfolio).