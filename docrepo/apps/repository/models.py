from django.db import models


class Folder(models.Model):
    """Folder model - contains documents and other folders."""

    name = models.CharField('Name', max_length=255)
    title = models.CharField('Title', max_length=255, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return self.name
