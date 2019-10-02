from django.db import models


class About(models.Model):
    types = (
        ('header', 'header'),
        ('carousel', 'carousel'),
        ('box', 'box'),
    )

    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    article_type = models.CharField(max_length=15, choices=types)
