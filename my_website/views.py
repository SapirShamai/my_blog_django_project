from django.http import HttpResponse
from django.urls import reverse


def home(request):
    response = [
        'Welcome to my website',
        '<a href="', reverse('home'), '">Go To Blog</a>'
    ]
    return HttpResponse(''.join(response))
