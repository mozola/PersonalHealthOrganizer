from django.db import models
from django.utils import timezone
from Meals.models import Meals


class SinglePlan(models.Model):
    plan_date = models.DateTimeField(default = timezone.now)
    meals = models.ManyToManyField(Meals)

    def __str__(self):
        return str('{} {}'.format(self.plan_date, self.meals))