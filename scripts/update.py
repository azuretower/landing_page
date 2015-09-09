#!/usr/bin/env python
import os
import subprocess

def pull():
    pull = subprocess.Popen(['git', 'pull'],
                        cwd='/sites/projects/landing_page/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = pull.communicate()
    return out, err

def collect():
    collect = subprocess.Popen(['/sites/virtualenvs/landing_page/bin/python', './manage.py', 'collectstatic', '--noinput'],
                        cwd='/sites/projects/landing_page/',
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
