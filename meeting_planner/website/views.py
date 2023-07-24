from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("this page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse(
        "Hello, this is a website that I'm trying to create using Django. By the way this is my dog's name")
