"""Admin module configs and registrations app models."""

from django.contrib import admin
from .models import Folder


admin.site.register(Folder)
