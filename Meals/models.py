# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum


class Component(models.Model):
    choices_list = (
        ('sztuk', 'sztuk'),
        ('gramy', 'gramy'),
        ('litry', 'litry')
    )
    name = models.CharField(max_length = 30)
    waste = models.FloatField()
    units = models.CharField(max_length = 10,
                            choices=choices_list)

    def __str__(self):
        return self.name

class Product(models.Model):
    choices_list = (
        ('sztuk', 'sztuk'),
        ('gramy', 'gramy'),
        ('litry', 'litry')
    )
    component = models.ForeignKey(Component)
    count = models.IntegerField()
    units = models.CharField(max_length = 10,
                            choices=choices_list)

    def __str__(self):
<<<<<<< HEAD
        return str(self.component)


    @classmethod
    def create(cls, component, count, units):
        product = cls(component=component, count=count, units = units)
        return product
=======
        return '{}\t{}\t{}'.format(self.component, self.count, self.units)
>>>>>>> d63415e96c9f861b3dc70247f25526a63ee5f312

class Meal(models.Model):

    choice_list = (
        ('sniadanie', 'sniadanie'),
        ('obiad', 'obiad'),
        ('kolacja', 'kolacja'),
    )

    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 500)
    products = models.ManyToManyField(Product)
    callories = models.CharField(max_length = 10)
    types = models.CharField(max_length=15,
                            choices=choice_list)
    image = models.ImageField(upload_to='Meals/static/jpg/',
                              default='static/jpg/')

    state = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, description, products, callories, types):
        products = cls(name=name,
                       description=description,
                       products = products,
                       callories = callories,
                       types=types)

        return products