# -*- coding: utf-8 -*-
from django.db import models
from django.template import loader


class Meals(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    components = models.CharField(max_length = 200)
    callories = models.CharField(max_length = 10)
    image = models.ImageField(upload_to = 'Meals/static/meals/image', default = 'Meals/static/meals/image')

    def __str__(self):
        return self.name