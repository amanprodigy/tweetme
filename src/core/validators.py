from django.forms import ValidationError
from .utils import get_urls


def checkurl(value):
    content = value
    if get_urls(content):
        raise ValidationError('Text cannot consist of urls')
    return value
