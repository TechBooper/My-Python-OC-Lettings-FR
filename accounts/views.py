"""
views.py for the 'profiles' application.

This module contains view functions responsible for handling requests 
related to user profiles, including:

- The `index` view: Renders the main landing page for profiles.
- The `profile` view: Renders an individual user's profile page.
"""

from django.shortcuts import get_object_or_404, render
from .models import Profile
from django.http import HttpResponse


def index(request):
    """
    Render the index page for the 'profiles' application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'profiles/index.html' template.
    """
    return render(request, "profiles/index.html")


def profile(request, username):
    """
    Render the profile page for a specific user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: The rendered 'profiles/profile.html' template,
        including the requested user's profile as context.

    Raises:
        Http404: If a `Profile` object matching the given username does not exist.
    """
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, "profiles/profile.html", {"profile": profile})
