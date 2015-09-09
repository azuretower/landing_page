#!/usr/bin/env python
import subprocess


def pull():
    pull = subprocess.Popen(['git', 'pull'],
                        cwd='/sites/projects/landing_page/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = pull.communicate()
    return out, err

def collect():
    collect = subprocess.Popen(['./manage.py', 'collectstatic'],
                        cwd='/sites/projects/landing_page/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = collect.commuincate()
    return out, err
