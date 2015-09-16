#!/usr/bin/env python
import os
import subprocess
from StringIO import StringIO
from django.conf import settings
from django.core.management import call_command


project_home = settings.BASE_DIR

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

def restart():
    restart = subprocess.Popen(['service', 'apache2', 'restart'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = restart.communicate()
    return out, err
