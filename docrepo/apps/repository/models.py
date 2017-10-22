"""Models module for Repository app."""
from django.contrib.auth.models import User
from django.db import models


class NamedModel(models.Model):
    """Abstract model having name and description fields."""
    name = models.CharField('Name', max_length=50, unique=True)
    description = models.TextField('Description', null=True, blank=True)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """Abstract model having created and modified timestamps."""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContentModel(models.Model):
    """Abstract model having a content file."""
    content_file = models.FileField(upload_to='content/%Y/%m/%d/%H/%M')

    class Meta:
        abstract = True


class OwnedModel(models.Model):
    """Abstract model with an owner user."""
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class Tenant(NamedModel, TimestampedModel, OwnedModel):
    """A domain that projects and users belong to."""
    domain = models.CharField('Domain Name', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return self.name


class Project(NamedModel, TimestampedModel, OwnedModel):
    """A site for categories and documents."""
    parent_tenant = models.ForeignKey('Tenant')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Category(NamedModel, TimestampedModel, OwnedModel):
    """A tag or folder or categorization that a document can belong to."""
    parent_project = models.ForeignKey('Project')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Document(NamedModel, TimestampedModel, OwnedModel):
    """A file for the repository that can have its own content, metadata,
    versions and depictions."""
    parent_categories = models.ManyToManyField('Category')
    title = models.CharField('Title', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name


class Facet(NamedModel):
    """A collection of properties that can be associated with a document."""
    document = models.ForeignKey('Document')

    class Meta:
        verbose_name = 'Facet'
        verbose_name_plural = 'Facets'

    def __str__(self):
        return self.name


class Property(models.Model):
    """A key/value pair property that can be associated with a facet."""
    facet = models.ForeignKey('Facet')
    name = models.CharField('Name', max_length=80)
    value = models.TextField('Value')
    data_type = models.CharField(
        'Data Type', max_length=30, choices=(
            ('int', 'int'),
            ('float', 'float'),
            ('string', 'string'),
            ('datetime', 'datetime'),
        )
    )

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return '{} : {}'.format(self.name, self.value)


class DocumentVersion(TimestampedModel, ContentModel):
    """The content file version for a particular document."""
    document = models.ForeignKey('Document')
    version = models.CharField('Version', max_length=12)

    class Meta:
        verbose_name = 'Document Version'
        verbose_name_plural = 'Document Versions'

    def __str__(self):
        return '{} / {}'.format(self.document.name, self.version)


class Depiction(TimestampedModel, ContentModel):
    """Version of content like an image taken of it or a PDF created for it."""
    document_version = models.ForeignKey('DocumentVersion')
    file_type = models.CharField(
        'File Type', max_length=30, choices=(
            ('image', 'image'),
            ('pdf', 'pdf'),
        )
    )

    class Meta:
        verbose_name = 'Depiction'
        verbose_name_plural = 'Depictions'

    def __str__(self):
        return '{} / {} / {}'.format(
            self.document_version.document.name,
            self.document_version.version,
            self.file_type,
        )
