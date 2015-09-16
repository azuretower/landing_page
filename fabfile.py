from fabric.api import local

def deploy(message='updates'):
    local('git add .')
    local('git commit -m "%s"' % message)
    local('git push')
