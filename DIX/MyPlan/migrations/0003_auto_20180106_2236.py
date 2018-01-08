# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPlan', '0002_singleplan_meal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleplan',
            name='meal_id',
            field=models.ForeignKey(to='Meals.Meals'),
        ),
    ]
