from django.shortcuts import render
from django.http import HttpResponse
from scripts import pull

def home(request):
    context = {}

    return render(request, 'index.html', context)

def update(request):
    context = {}
    response, error = pull.update()
    context['response'] = response
    context['error'] = error
    return render(request, 'response.html', context)
