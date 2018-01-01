from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>To jest strona z cwiczeniami</h1>")
