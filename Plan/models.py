from django.db import models
from django import forms
from django.utils import timezone
from django.conf import settings
from Meal.models import Meal


USER = settings.AUTH_USER_MODEL


class SinglePlan(models.Model):
    plan_date = models.DateField(default = timezone.now)
    meals = models.ManyToManyField(Meal)
    state = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.plan_date}'


class Sprint(models.Model):

    choices = (
        ('Nowy', 'nowy'),
        ('Rozpoczety', 'rozpoczety'),
        ('Skonczony', 'skonczony')
    )
    sprint_user = models.ForeignKey(USER, default=1, null=True, on_delete=models.CASCADE)
    sprint_name = models.CharField(max_length = 20)
    sprint_parameters = models.ManyToManyField(SinglePlan)
    sprint_status = models.CharField(choices=choices, default=True, max_length=10)
