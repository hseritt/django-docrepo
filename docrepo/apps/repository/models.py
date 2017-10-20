"""Models module for Repository app."""
from django.db import models


class NamedModel(models.Model):
    name = models.CharField('Name', max_length=50, unique=True)
    description = models.TextField('Description', null=True, blank=True)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tenant(NamedModel, TimestampedModel):
    domain = models.CharField('Domain Name', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return self.name


class Project(NamedModel, TimestampedModel):
    parent_tenant = models.ForeignKey('Tenant')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Category(NamedModel, TimestampedModel):
    parent_project = models.ForeignKey('Project')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Document(NamedModel, TimestampedModel):
    parent_categories = models.ManyToManyField('Category')
    title = models.CharField('Title', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name


class Facet(NamedModel):
    document = models.ForeignKey('Document')

    class Meta:
        verbose_name = 'Facet'
        verbose_name_plural = 'Facets'

    def __str__(self):
        return self.name


class Property(models.Model):
    facet = models.ForeignKey('Facet')
    name = models.CharField('Name', max_length=80)
    value = models.TextField('Value')
    data_type = models.CharField('Data Type', max_length=30, choices=(
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
        return self.name
