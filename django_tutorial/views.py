from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("<h1>Hello world, this is my homepage</h1>")
    # return render(request, template_name='home/home.html')



