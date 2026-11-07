
"""
Application configuration for the VIRA core app.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "هسته اصلی سایت ویرا"
