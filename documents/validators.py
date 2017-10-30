import magic
from django.core.exceptions import ValidationError

# Validates if uploaded file is either pdf or jpg
def validate_mime_type(value):
    supported_types = ['application/pdf']
    with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
        mime_type = m.id_buffer(value.file.read(1024))
        value.file.seek(0)
    if mime_type not in supported_types:
        raise ValidationError(u'Unsupported file. Only PDF files can be uploaded!')