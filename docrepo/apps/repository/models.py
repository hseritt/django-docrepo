"""Models module for Repository app."""
from django.db import models


class ContentNode(models.Model):
    """Abstract model"""
    name = models.CharField('Name', max_length=255)
    title = models.CharField('Title', max_length=255, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    class Meta:
        abstract = True


class Folder(ContentNode):
    """Folder model - contains documents and other folders."""
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return self.name


class Document(ContentNode):
    """Document model - represents a document and the versions associated with it."""
    parent = models.ForeignKey('Folder')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name
