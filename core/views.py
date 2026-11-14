
"""
Views for the VIRA core application.
"""

from django.http import HttpResponse


def home(request):
    """
    Temporary homepage view for testing the core application.
    """
    return HttpResponse("هسته اصلی وب‌سایت ویرا با موفقیت اجرا شد.")
