from django.urls import path
from . import views

# Define the namespace for this app's URLs
app_name = "lettings"

# URL patterns for the 'lettings' app
# - Route for the index view:
#   Displays a list of all lettings.
#   URL: /
#   View: views.index
#   Name: "index"
#
# - Route for the letting detail view:
#   Displays detailed information for a specific letting.
#   URL: /<letting_id>/
#   View: views.letting
#   Name: "letting"
#   Parameters:
#     letting_id (int): ID of the letting to be displayed.

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
