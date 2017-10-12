"""Tests module for the repository app."""

from django.test import TestCase
from .models import Folder


class RepositoryModelsTestCase(TestCase):
    """TestCase class for Repository app models."""

    def setUp(self):
        pass

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
