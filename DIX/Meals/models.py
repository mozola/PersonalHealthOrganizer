# -*- coding: utf-8 -*-
from django.db import models
from django.template import loader


class Meals(models.Model):

    choice_list = (
        ('sniadanie', 'sniadanie'),
        ('obiad', 'obiad'),
        ('kolacja', 'kolacja'),
    )

    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    components = models.CharField(max_length = 400)
    callories = models.CharField(max_length = 10)
    type = models.CharField(
        max_length=10,
        choices=choice_list
    )
    image = models.ImageField(upload_to = 'Meals/static/meals/image', default = 'Meals/static/meals/image')

    def __str__(self):
        return self.name

class Components(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

