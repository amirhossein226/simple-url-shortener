import random
import string


url_list = {'ABcd1234': 'https://www.asre-amn.com/'}


def random_key_generator():
    while True:
        random_key = ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=8
        ))
        if not check_existence(key=random_key):
            return random_key


def check_existence(*, key=None, old_url=None):

    for short_key, url in url_list.items():
        if key == short_key or url == old_url:
            return short_key
    return None


def save_url(key, value):
    url_list[key] = value


def get_url(key):
    return url_list.get(key)
