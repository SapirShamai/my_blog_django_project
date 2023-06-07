from django.http import HttpResponse
from django.urls import reverse


def home(request):
    response = [
        'Welcome to my website',
        '<a href="', reverse('blogs:blog'), '">Go To Blog</a>'
    ]
    return HttpResponse(''.join(response))
