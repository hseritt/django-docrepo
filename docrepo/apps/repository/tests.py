"""Tests module for the repository app."""

from django.test import TestCase
from .models import Document, Folder


class RepositoryModelsTestCase(TestCase):
    """TestCase class for Repository app models."""

    def setUp(self):
        self.root_folder = Folder.objects.create(
            name='ROOT', title='Root Folder', description='This is the root folder'
        )

    def test_add_folder_model(self):
        """Test for adding Folder model."""
        self.assertTrue(
            Folder.objects.create(
                name='Folder1', title='Folder #1', description='This is folder #1'
            )
        )

        folder = Folder.objects.get(name='Folder1')
        self.assertEqual(folder.name, 'Folder1')
        self.assertEqual(folder.title, 'Folder #1')
        self.assertEqual(folder.description, 'This is folder #1')

    def test_add_document_model(self):
        """Test for adding simple Document model."""
        self.assertTrue(
            Document.objects.create(
                name='Document1.txt',
                title='Document #1',
                description='This is document #1',
                parent=self.root_folder,
            )
        )

        document = Document.objects.get(name='Document1.txt')
        self.assertEqual(document.name, 'Document1.txt')
        self.assertEqual(document.title, 'Document #1')
        self.assertEqual(document.description, 'This is document #1')
