#!/usr/bin/env python
import os
import subprocess
from django.conf import settings


project_home = os.environ['PROJECT_HOME']
env_home = os.environ['WORKON_HOME']
project_name = settings.PROJECT_NAME

def chown():
    chown = subprocess.Popen(['chown', '-R', 'www-data:www-data', project_name + '/'],
                        cwd=project_home,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = chown.communicate()
    return out, err

def pull():
    pull = subprocess.Popen(['git', 'pull'],
                        cwd=project_home + '/' + project_name,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = pull.communicate()
    return out, err

def collect():
    collect = subprocess.Popen([env_home + '/' + project_name + '/bin/python', './manage.py', 'collectstatic', '--noinput'],
                        cwd=project_home + '/' + project_name + '/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = collect.communicate()
    return out, err

def restart():
    restart = subprocess.Popen(['service', 'apache2', 'restart'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = restart.communicate()
    return out, err
