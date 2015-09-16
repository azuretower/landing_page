#!/usr/bin/env python
import os
import subprocess
import StringIO
from django.conf import settings
from django.core.management import call_command



project_home = settings.BASE_DIR

# def chown():
#     chown = subprocess.Popen(['chown', '-R', 'www-data:www-data', project_name + '/'],
#                         cwd=project_home,
#                         stdout=subprocess.PIPE, 
#                         stderr=subprocess.PIPE)

#     out, err = chown.communicate()
#     return out, err

def pull():
    pull = subprocess.Popen(['git', 'pull'],
                        cwd=project_home,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = pull.communicate()
    return out, err

def collect():

    out = StringIO()
    err = StringIO()
    call_command('collectstatic', interactive=False, stdout=out, stderr=err)

    return out.getvalue(), err.getvalue()
    # collect = subprocess.Popen([env_home + '/' + project_name + '/bin/python', './manage.py', 'collectstatic', '--noinput'],
    #                     cwd=project_home + '/' + project_name + '/',
    #                     stdout=subprocess.PIPE, 
    #                     stderr=subprocess.PIPE)

    # out, err = collect.communicate()

def restart():
    restart = subprocess.Popen(['service', 'apache2', 'restart'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = restart.communicate()
    return out, err
