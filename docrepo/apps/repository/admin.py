"""Admin module configs and registrations app models."""

from django.contrib import admin
from .models import (
    Tenant, Project, Category, Document, Facet,
    Property, DocumentVersion, Depiction
)


admin.site.register(Tenant)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Document)
admin.site.register(Facet)
admin.site.register(Property)
admin.site.register(DocumentVersion)
admin.site.register(Depiction)
