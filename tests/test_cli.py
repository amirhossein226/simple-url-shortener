from shortener.shortener import __version__
from bddcli import Given, Application, stdout, stderr, when, status


def test_app_cli():
    cliapp = Application('shortener', 'shortener.shortener:app.climain')
    with Given(cliapp, 'version'):
        assert stderr == ''
        assert status == 0
        assert stdout.strip() == __version__

        when('v')
        assert stderr == ''
        assert status == 0
        assert stdout.strip() == __version__

        when('ver')
        assert stderr == ''
        assert status == 0
        assert stdout.strip() == __version__

    with Given(cliapp, 'invalidcommand'):
        assert status != 0
        assert stderr != ''
