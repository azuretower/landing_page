from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from scripts import update


def update_view(request):
    # checkout this site to figure out better security
    # http://eli.thegreenplace.net/2014/07/09/payload-server-in-python-3-for-github-webhooks
    if request.method == 'POST' or 'GET':
        context = {}
        pull_response, pull_error = update.pull()
        collect_response, collect_error = update.collect()
        restart_response, restart_error = update.restart()
        context['pull'] = pull_response
        context['pull_error'] = pull_error
        context['collect'] = collect_response
        context['collect_error'] = collect_error
        context['restart'] = restart_response
        context['restart_error'] = restart_error
        return render(request, 'response.html', context)
