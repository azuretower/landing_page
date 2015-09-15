This module relies on the file structure that virtualenvwrapper sets up

add 'github_webhooks' to your installed apps

add url(r'^', include('github_webhooks.urls')) to your project level urls.py

add PROJECT_NAME = '' to your settings.py file, the name should be the file name 
    inside your projects directory
