from django.shortcuts import render
from django.http import HttpResponse
from scripts import pull

def home(request):
    context = {}

    return render(request, 'index.html', context)

def update(request):
    context = {}
    response = pull.update()
    context['response'] = response
    return render(request, 'response.html', context)
