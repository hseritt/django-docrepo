"""Tests module for the repository app."""
import os
from django.contrib.auth.models import User
from django.core.files import File
from django.test import TestCase
from docrepo.settings import INITIAL_DOCUMENT_VERSION
from .models import Tenant, Project, Category, Document, DocumentVersion
from .services import add_document


class RepositoryModelsTestCase(TestCase):
    """TestCase class for Repository app models."""

    def setUp(self):
        pass

class RepositoryServicesTestCase(TestCase):
    """TestCase for service functions."""

    def setUp(self):

        self.admin_user = User.objects.create(username='admin', email='admin@localhost')

        tenant = Tenant.objects.create(
            name='TestTenant',
            owner=self.admin_user,
            domain='localhost',
            description='This is a test tenant.'
        )

        project = Project.objects.create(
            name='TestProject',
            owner=self.admin_user,
            parent_tenant=tenant,
            description='This is a test project.'
        )

        category1 = Category.objects.create(
            name='TestCategory1',
            owner=self.admin_user,
            description='This is a test category #1.',
            parent_project=project
        )

        self.categories = []
        self.categories.append(category1)



    def test_add_document(self):
        """Test for add_document() from services module."""
        file_name = 'samples/testfile1.txt'
        file_name_str = os.path.basename(file_name)

        with open(file_name, 'r+') as f:

            add_document(
                name=file_name_str,
                owner=self.admin_user,
                content_file=File(f),
                categories=self.categories,
            )

        document = Document.objects.get(name=file_name_str)
        self.assertTrue(document)

        document_versions = DocumentVersion.objects.filter(document=document)
        self.assertEqual(document_versions[0].version, INITIAL_DOCUMENT_VERSION)
