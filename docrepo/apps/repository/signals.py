"""Signals module for repository app."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document


@receiver(post_save, sender=Document)
def index_document_post(sender, instance, **kwargs):
    instance.indexing()
