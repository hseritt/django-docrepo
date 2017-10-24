"""Services module for handling some model functionality."""
from docrepo.settings import INITIAL_DOCUMENT_VERSION
from .models import Document, DocumentVersion


def add_document(name, owner, content_file, categories=None, **kwargs):
    """Add a new document with new document version."""
    document = Document()
    document.name = name
    document.owner = owner

    for k, v in kwargs.items():
        setattr(document, k, v)
    document.save()

    if categories:
        for category in categories:
            document.parent_categories.add(category)
        document.save()

    document_version = DocumentVersion()
    document_version.content_file = content_file
    document_version.document = document
    document_version.version = INITIAL_DOCUMENT_VERSION
    document_version.save()
