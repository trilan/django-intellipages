from paver.easy import *


@task
def build():
    """Bootstrap's and init's buildout."""
    sh('python bootstrap.py -d')
    sh('./bin/buildout')


@task
def clean():
    """Clean's up working directory from buildout staff."""
    path('bin').rmtree()
    path('develop-eggs').rmtree()
    path('dist').rmtree()
    path('eggs').rmtree()
    path('parts').rmtree()
    path('src/django_intellipages.egg-info').rmtree()
    path('.installed.cfg').remove()
    [pyc.remove() for pyc in path('.').walkfiles('*.pyc')]
    [pyo.remove() for pyo in path('.').walkfiles('*.pyo')]