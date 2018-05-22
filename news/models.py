from django.db import models

class SinglNews(models.Model):
    title = models.CharField(max_length=100)
    contain = models.CharField(max_length=400)
    author = models.CharField(max_length=100)