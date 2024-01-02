import os
import random

from django import template
import hashlib

from main.settings import BASE_DIR

register = template.Library()

def hash_file(file):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()

@register.simple_tag
def break_cache(url) -> str:
    print(url)
    path = str(BASE_DIR) + '/frontend' + url
    print(BASE_DIR)

    print(path)

    hash = hash_file(path)

    return url + '?' + hash
