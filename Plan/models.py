#coding=utf-8

from django.db import models
from django import forms
from django.utils import timezone
from Meal.models import Meal


class SinglePlan(models.Model):
    plan_date = models.DateField(default = timezone.now)
    meals = models.ManyToManyField(Meal)
    state = models.BooleanField(default=False)


class Sprint(models.Model):

    choices = (
        ('Nowy', 'nowy'),
        ('Rozpoczety', 'rozpoczety'),
        ('Skonczony', 'skonczony')
    )
    sprint_id = models.IntegerField()
    sprint_name = models.CharField(max_length = 20)
    sprint_parameters = models.ManyToManyField(SinglePlan)
    sprint_status = models.CharField(choices=choices , max_length=10)
