"""Serializers module for use with API app."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.repository.models import (
    Tenant, Project, Category, Document, Facet,
    Property, DocumentVersion, Depiction
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model = Group
        fields = ('url', 'name')


class TenantSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Tenant model."""
    class Meta:
        model = Tenant
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'domain',
        )


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Project model."""
    class Meta:
        model = Project
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'parent_tenant',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'parent_project',
        )


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Document model."""
    class Meta:
        model = Document
        fields = (
            'name', 'description', 'created', 'modified',
            'owner', 'parent_categories', 'title',
        )


class FacetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Facet model."""
    class Meta:
        model = Facet
        fields = (
            'name', 'description', 'document',
        )


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Property model."""
    class Meta:
        model = Property
        fields = (
            'facet', 'name', 'value', 'data_type',
        )


class DocumentVersionSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for DocumentVersion model."""
    class Meta:
        model = DocumentVersion
        fields = (
            'created', 'modified', 'content_file', 'document', 'version',
        )


class DepictionSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Depiction model."""
    class Meta:
        model = Depiction
        fields = (
            'created', 'modified', 'content_file', 'document_version', 'file_type',
        )
