from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Renders the index page for lettings, displaying a list of all available lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'lettings/index.html' template with a list of lettings.
    """
    lettings = Letting.objects.all()
    return render(request, "lettings/index.html", {"lettings": lettings})


def letting(request, letting_id):
    """
    Renders the detailed page for a specific letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered 'lettings/letting.html' template with the letting details.

    Raises:
        Http404: If the letting with the given ID does not exist.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    return render(request, "lettings/letting.html", {"letting": letting})
