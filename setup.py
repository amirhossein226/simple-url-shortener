from setuptools import setup
from os import path

requirements_file = path.join(path.dirname(__file__),
                              'requirements.txt')
with open(requirements_file, 'r') as f:
    required_libs = [
        line.strip()
        for line in f.readlines()
        if line.strip() and not line.startswith('#')
    ]
setup(
    name='shortener',
    version='1.0.0',
    install_requires=required_libs,
    py_modules=['shortener'],
    entry_points={
        "console_scripts": [
            "shortener=shortener:app.climain"
        ]
    }
)
