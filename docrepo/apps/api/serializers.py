"""Serializers module for use with API app."""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.repository.models import (
    Tenant, Project, Category, Document, Facet,
    Property, DocumentVersion, Depiction
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TenantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'domain',
        )


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'parent_tenant',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name', 'description', 'created', 'modified', 'owner', 'parent_project',
        )


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = (
            'name', 'description', 'created', 'modified',
            'owner', 'parent_categories', 'title',
        )


class FacetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facet
        fields = (
            'name', 'description', 'document',
        )


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = (
            'facet', 'name', 'value', 'data_type',
        )


class DocumentVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentVersion
        fields = (
            'created', 'modified', 'content_file', 'document', 'version',
        )


class DepictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Depiction
        fields = (
            'created', 'modified', 'content_file', 'document_version', 'file_type',
        )
