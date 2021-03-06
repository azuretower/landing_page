from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from contextlib import contextmanager as _contextmanager

env.hosts = ['root@ryanmerrill.me']
env.user = 'www-data'
env.directory = '/sites/projects/landing_page'
env.activate = 'source /sites/virtualenvs/landing_page/bin/activate'

def push(message='updates'):
    local('git add .')
    local('git commit -m "%s"' % message)
    local('git push')


def collect_static():
    with virtualenv():
        run('./manage.py collectstatic --noinput')

def install_requirements():
    #Install the pip requirements listed in the reqs.txt file.
    with virtualenv():
        run('pip install -r reqs.txt')

def migrate():
    with virtualenv():
        run('./manage.py migrate')

def pull():
    code_dir = '/sites/projects/landing_page'
    with cd(code_dir):
        sudo('git pull', user='www-data')

    code_dir = '/sites/projects/landing_page/github_webhooks'
    with cd(code_dir):
        sudo('git pull', user='www-data')
    
def deploy():
    pull()
    install_requirements()
    collect_static()
    sudo('service apache2 restart')

@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield
