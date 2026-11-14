
"""
URL configuration for the VIRA core application.
"""

from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
]
