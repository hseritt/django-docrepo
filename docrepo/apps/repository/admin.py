"""Admin module configs and registrations app models."""

from django.contrib import admin
from .models import Document, Folder


admin.site.register(Folder)
admin.site.register(Document)
