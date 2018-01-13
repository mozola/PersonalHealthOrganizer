# -*- coding: utf-8 -*-
from django.db import models
from django.template import loader
import os
from django.conf import settings

class Components(models.Model):
    name = models.CharField(max_length = 30)
    waste = models.FloatField()
    units = models.CharField(max_length = 10)
    def __str__(self):
        return self.name


class Meals(models.Model):

    choice_list = (
        ('sniadanie', 'sniadanie'),
        ('obiad', 'obiad'),
        ('kolacja', 'kolacja'),
    )

    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    components = models.ManyToManyField(Components)
    callories = models.CharField(max_length = 10)
    type = models.CharField(
        max_length=10,
        choices=choice_list
    )
    image = models.ImageField(upload_to = 'Meals/static/jpg/',
                              default = 'static/jpg/')

    def __str__(self):
        return self.name


