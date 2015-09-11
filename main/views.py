from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    context = {}

    return render(request, 'index.html', context)

def message(request):
    context = {}

    from_address = 'azuretower7@gmail.com'
    to_address = 'ryan.merrill215@gmail.com'

    if request.method == 'POST':

        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = 'Message from ' + name + ' - ' + email + '\n\n'
        message += request.POST.get('message')
        print subject
        print name
        print email
        print message

        send_mail(subject, message, from_address, [to_address], fail_silently=False)
        return HttpResponse(status=200)

    return HttpResponse(status=503)
