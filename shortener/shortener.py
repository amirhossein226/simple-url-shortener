#! /usr/bin/env python3

from yhttp.core import Application, text, statuses, guard
import sys
from easycli import SubCommand

from .tools import check_existence, random_key_generator, save_url, get_url

app = Application()
base_url = 'http://localhost:8080/'

__version__ = '1.0.0'


class Version(SubCommand):
    __command__ = 'version'
    __aliases__ = ['v', 'ver']

    def __call__(self, *args):
        print(__version__)


app.cliarguments.append(Version)


@app.route(r'/url_shortener/?', verb='post')
@app.bodyguard(
    fields=(
        guard.String('url', optional=False),
    ),
    strict=True
)
@text
def get_short_url(req):
    form = req.getform()
    old_url = form['url']

    # None if the old_url not exits on url_list and will return key otherwise
    key = check_existence(old_url=old_url)
    if key:
        return base_url + key

    print("Generating short url...")
    random_key = random_key_generator()

    save_url(random_key, old_url)

    return base_url + random_key


@app.route(r'/([a-zA-Z0-9]{8})/?', verb='get')
@text
def redirect_to_original(req, key):
    original_url = get_url(key)

    if not original_url:
        raise statuses.notfound()

    raise statuses.status(301, f'You are redirecting to \
                          {original_url} right now...')


app.ready()

if __name__ == "__main__":
    sys.exit(app.climain())
