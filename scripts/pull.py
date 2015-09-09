#!/usr/bin/env python
import os
import subprocess


def update():
    p = subprocess.Popen(['git', 'pull'], cwd='/sites/projects/landing_page/', stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
    out, err = p.communicate() 
    return out, err





    # response = os.system('git pull')
    # print 'hi'
    # return response
