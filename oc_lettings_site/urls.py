"""
This module defines the URL configuration for the main 'oc_lettings_site' application.

It includes:
- A root path ("") that routes to the `home` view.
- A path ("lettings/") that includes the URL patterns of the 'property_lettings' application.
- A path ("profiles/") that includes the URL patterns of the 'accounts' application.
- A path ("admin/") that routes to the Django admin site.
"""

from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#: A list of URL pattern definitions for the entire project.
urlpatterns = [
    # Routes the root URL to the `home` view in the current application.
    path("", views.home, name="index"),
    # Includes the URL patterns from the 'property_lettings' app,
    # accessible at the 'lettings/' sub-path.
    path("lettings/", include("property_lettings.urls", namespace="lettings")),
    # Includes the URL patterns from the 'accounts' app,
    # accessible at the 'profiles/' sub-path.
    path("profiles/", include("accounts.urls", namespace="profiles")),
    # Routes to the Django admin interface.
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
