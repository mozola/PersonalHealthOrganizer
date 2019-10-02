from django.shortcuts import render
from .models import About


def index(request):
    return render(request, 'About/about_main.html', {'contents': About.objects.all(),
                                                     'header': 'header'})
