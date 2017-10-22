"""A messages file to hold values for repository models strings."""

MSG = {
    'model_meta_name': 'Name',
    'model_meta_title': 'Title',
    'model_meta_description': 'Description',
    'model_meta_content_dir': 'content/%Y/%m/%d/%H/%M',
    'tenant': {
        'domain': 'Domain Name',
        'verbose_name': 'Tenant',
        'verbose_name_plural': 'Tenants',
    },
    'project': {
        'verbose_name': 'Project',
        'verbose_name_plural': 'Projects',
    },
    'category': {
        'verbose_name': 'Category',
        'verbose_name_plural': 'Categories',
    },
    'document': {
        'verbose_name': 'Document',
        'verbose_name_plural': 'Documents',
    },
    'facet': {
        'verbose_name': 'Facet',
        'verbose_name_plural': 'Facets',
    },
    'property': {
        'name': 'Name',
        'value': 'Value',
        'data_type': 'Data Type',
        'choices': (
            ('int', 'int'),
            ('float', 'float'),
            ('string', 'string'),
            ('datetime', 'datetime'),
        ),
        'verbose_name': 'Property',
        'verbose_name_plural': 'Properties',
    },
    'document_version': {
        'version': 'Version',
        'verbose_name': 'Document Version',
        'verbose_name_plural': 'Document Versions',
    },
    'depiction': {
        'file_type': 'File Type',
        'choices': (
            ('image', 'image'),
            ('pdf', 'pdf'),
        ),
        'verbose_name': 'Depiction',
        'verbose_name_plural': 'Depictions',
    },
}
