from django.shortcuts import render
from django.http import HttpResponse
from scripts import pull

def home(request):
    context = {}

    return render(request, 'index.html', context)

def update(request):
    pull.update()
    return HttpResponse(status=200)
