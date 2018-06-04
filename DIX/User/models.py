from django.db import models
from django.forms import ModelForm

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length=20)
    mail = models.EmailField()
