from shortener.shortener import __version__
from bddcli import Given, Application, stdout, stderr, when, status


def test_app_cli():
    cliapp = Application('shortener', 'shortener.shortener:app.climain')
    with Given(cliapp, 'version'):
        assert stderr == ''
        assert status == 0
        assert stdout == __version__ + '\n'

        when('v')
        assert stderr == ''
        assert status == 0
        assert stdout == __version__ + '\n'

        when('ver')
        assert stderr == ''
        assert status == 0
        assert stdout == __version__ + '\n'
