from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello Project 3</h1>')
