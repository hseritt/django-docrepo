from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class DocumentIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'document-index'


def bulk_indexing():
    DocumentIndex.init()
    es = Elasticsearch()
    bulk(
        client=es, actions=(
            b.indexing() for b in models.Document.objects.all().iterator()
        )
    )
