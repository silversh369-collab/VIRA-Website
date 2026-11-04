
"""
WSGI config for VIRA website.
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vira_site.settings")

application = get_wsgi_application()
