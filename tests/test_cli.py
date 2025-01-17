from shortener import app
from bddcli import Given, Application, stdout, stderr, when, status
from easycli import SubCommand

__version__ = '1.0.0'

class Version(SubCommand):
    __command__ = 'version'
    __aliases__ = ['v', 'ver']

    def __call__(self, args):
        print(__version__)

app.cliarguments.append(Version)



def test_app_cli():
    cliapp = Application('./shortener', 'shortener:app.climain')
    with Given(cliapp, 'version'):
        assert status == 0
        assert stdout == __version__ + '\n' 

        
