import re

URL_REGEX = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'


def get_urls(url):
    return re.findall(URL_REGEX, url)
