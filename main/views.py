from django.shortcuts import render
from django.http import HttpResponse
from scripts import update

def home(request):
    context = {}

    return render(request, 'index.html', context)

def update_view(request):
    context = {}
    pull_response, pull_error = update.pull()
    # collect_response, collect_error = update.collect()
    context['pull'] = pull_response
    context['pull_error'] = pull_error
    # context['collect'] = collect_response
    # context['collect_error'] = collect_error
    return render(request, 'response.html', context)
