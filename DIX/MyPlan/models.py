#coding=utf-8

from django.db import models
from django import forms
from django.utils import timezone
from Meals.models import Meals


class SinglePlan(models.Model):
    plan_date = models.DateField(default = timezone.now)
    meals = models.ManyToManyField(Meals)

    def __str__(self):
        return str('{} {}'.format(self.plan_date, self.meals))


class Sprints(models.Model):

    choices = (
        ('Nowy', 'nowy'),
        ('Rozpoczety', 'rozpoczety'),
        ('Skonczony', 'skonczony')
    )
    sprint_id = models.IntegerField()
    sprint_name = models.CharField(max_length = 20)
    sprint_parameters = models.ManyToManyField(SinglePlan)
    sprint_status = models.CharField(choices=choices , max_length=10)

    def __str__(self):
        return str('Id: {}, Name: {}, State: {}'.format(self.sprint_id, self.sprint_name, self.sprint_status))

