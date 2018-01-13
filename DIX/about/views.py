from django.shortcuts import render
from django.http import HttpRequest
from models import About

def index(request):
    return render(request, 'about/index.html', {'contents': About.objects.all()})