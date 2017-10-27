"""Models module for Repository app."""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from docrepo.settings import INITIAL_DOCUMENT_VERSION
from .messages.models import MSG


class NamedModel(models.Model):
    """Abstract model having name and description fields."""
    name = models.CharField(
        MSG['model_meta_name'], max_length=50, unique=True)
    description = models.TextField(
        MSG['model_meta_description'], null=True, blank=True)

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
    content_file = models.FileField(
        upload_to=MSG['model_meta_content_dir'])

    class Meta:
        abstract = True


class OwnedModel(models.Model):
    """Abstract model with an owner user."""
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class Tenant(NamedModel, TimestampedModel, OwnedModel):
    """A domain that projects and users belong to."""
    domain = models.CharField(
        MSG['tenant']['domain'], max_length=255, unique=True)

    class Meta:
        verbose_name = MSG['tenant']['verbose_name']
        verbose_name_plural = MSG['tenant']['verbose_name_plural']

    def __str__(self):
        return self.name


class Project(NamedModel, TimestampedModel, OwnedModel):
    """A site for categories and documents."""
    parent_tenant = models.ForeignKey('Tenant')

    class Meta:
        verbose_name = MSG['project']['verbose_name']
        verbose_name_plural = MSG['project']['verbose_name_plural']

    def __str__(self):
        return self.name


class Category(NamedModel, TimestampedModel, OwnedModel):
    """A tag or folder or categorization that a document can belong to."""
    parent_project = models.ForeignKey('Project')

    class Meta:
        verbose_name = MSG['category']['verbose_name']
        verbose_name_plural = MSG['category']['verbose_name_plural']

    def __str__(self):
        return self.name


class Document(NamedModel, TimestampedModel, OwnedModel):
    """A file for the repository that can have its own content, metadata,
    versions and depictions."""
    parent_categories = models.ManyToManyField('Category')
    title = models.CharField(
        MSG['model_meta_title'], max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = MSG['document']['verbose_name']
        verbose_name_plural = MSG['document']['verbose_name_plural']

    def __str__(self):
        return self.name


class Facet(NamedModel):
    """A collection of properties that can be associated with a document."""
    document = models.ManyToManyField('Document')

    class Meta:
        verbose_name = MSG['facet']['verbose_name']
        verbose_name_plural = MSG['facet']['verbose_name_plural']

    def __str__(self):
        return self.name


class Property(models.Model):
    """A key/value pair property that can be associated with a facet."""
    facet = models.ForeignKey('Facet')
    name = models.CharField(MSG['property']['name'], max_length=80)
    value = models.TextField(MSG['property']['value'])
    data_type = models.CharField(
        MSG['property']['data_type'],
        max_length=30,
        choices=MSG['property']['choices']
    )

    class Meta:
        verbose_name = MSG['property']['verbose_name']
        verbose_name_plural = MSG['property']['verbose_name_plural']

    def __str__(self):
        return '{} : {}'.format(self.name, self.value)


class DocumentVersion(TimestampedModel, ContentModel):
    """The content file version for a particular document."""
    document = models.ForeignKey('Document')
    version = models.CharField(
        MSG['document_version']['version'], max_length=12)

    class Meta:
        verbose_name = MSG['document_version']['verbose_name']
        verbose_name_plural = MSG['document_version']['verbose_name_plural']

    def __str__(self):
        return '{} / {}'.format(self.document.name, self.version)


class Depiction(TimestampedModel, ContentModel):
    """Version of content like an image taken of it or a PDF created for it."""
    document_version = models.ForeignKey('DocumentVersion')
    file_type = models.CharField(
        MSG['depiction']['file_type'],
        max_length=30,
        choices=MSG['depiction']['choices'],
    )

    class Meta:
        verbose_name = MSG['depiction']['verbose_name']
        verbose_name_plural = MSG['depiction']['verbose_name_plural']

    def __str__(self):
        return '{} / {} / {}'.format(
            self.document_version.document.name,
            self.document_version.version,
            self.file_type,
        )


class UserProfile(TimestampedModel):
    """User profile for user accounts."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('Bio', null=True, blank=True)
    location = models.CharField('Location', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username


def get_next_version(version, mode='minor'):
    """Returns expected next version of document based on mode."""
    major, minor, patch = map(int, version.split('.'))
    if mode == 'minor':
        minor += 1
    elif mode == 'patch':
        patch += 1
    else:
        major += 1
    return f'{major}.{minor}.{patch}'


def get_latest_version(document):
    """Returns latest version of document versions associated with
    this document."""
    try:
        latest_version = DocumentVersion.objects.filter(
            document=document
        ).order_by('-created')[0].version
    except IndexError:
        latest_version = INITIAL_DOCUMENT_VERSION
    return latest_version


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Creates a user profile when a user is created."""
    # pylint: disable=W0612,W0613
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    """Save user profile pointer on save for user."""
    # pylint: disable=W0612,W0613
    instance.userprofile.save()


@receiver(post_save, sender=Document)
def create_document(instance, created, **kwargs):
    """Creates a document version when a document is created."""
    # pylint: disable=W0612,W0613
    if created:
        DocumentVersion.objects.create(
            document=instance,
            version=INITIAL_DOCUMENT_VERSION
        )
