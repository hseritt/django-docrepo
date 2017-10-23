"""Views module for API app."""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.api.serializers import (
    UserSerializer, GroupSerializer, TenantSerializer, ProjectSerializer,
    CategorySerializer, DocumentSerializer, FacetSerializer,
    PropertySerializer, DocumentVersionSerializer, DepictionSerializer
)
from apps.repository.models import (
    Tenant, Project, Category, Document,
    Facet, Property, DocumentVersion, Depiction,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TenantViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Tenants.
    """
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class FacetViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Facet.
    """
    queryset = Facet.objects.all()
    serializer_class = FacetSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Properties.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class DocumentVersionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Properties.
    """
    queryset = DocumentVersion.objects.all()
    serializer_class = DocumentVersionSerializer


class DepictionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Properties.
    """
    queryset = Depiction.objects.all()
    serializer_class = DepictionSerializer
