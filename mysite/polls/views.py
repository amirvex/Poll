from multiprocessing.spawn import import_main_path
from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Members


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def index(request):
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["firstname"]
    return HttpResponse(output)


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
