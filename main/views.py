from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from scripts import update

def home(request):
    context = {}

    return render(request, 'index.html', context)

@csrf_exempt
def update_view(request):
    if request.method == 'POST'
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
