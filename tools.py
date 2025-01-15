import random
import string
from .shortener import url_list

def random_key_generator():
    while True:
        random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if not check_existence(key=random_key):
            return random_key


def check_existence(*, key=None, old_url=None):
    for short_key, url in url_list.items():
        if key == short_key or url == old_url:
            return key

    return None
