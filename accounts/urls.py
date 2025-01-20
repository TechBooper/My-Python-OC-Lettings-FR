"""
urls.py for the 'profiles' application.

This module defines the URL configuration for the 'profiles' app. It includes:

- A root path ("") that routes to the `index` view.
- A dynamic path ("<str:username>/") that routes to the `profile` view, 
  passing the user's username as a string parameter.
"""

from django.urls import path
from . import views

#: The name used to refer to these URL patterns in other parts of the project.
app_name = "profiles"

#: A list of URL pattern definitions for the 'profiles' application.
urlpatterns = [
    # Routes the root URL ("profiles/") to the `index` view.
    path("", views.index, name="index"),

    # Routes URLs of the form ("profiles/<str:username>/") to the `profile` view.
    # The username is captured from the URL and passed to the view.
    path("<str:username>/", views.profile, name="profile"),
]
