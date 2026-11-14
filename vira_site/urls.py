
"""
URL configuration for VIRA website.
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Official Django administration panel
    path("django-admin/", admin.site.urls),

    # Core application routes
    path("", include("core.urls")),
]
