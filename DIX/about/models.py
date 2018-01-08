from django.db import models

class About(models.Model):
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length = 500)
