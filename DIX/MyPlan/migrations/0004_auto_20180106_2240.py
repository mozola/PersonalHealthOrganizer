# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0003_auto_20180105_1642'),
        ('MyPlan', '0003_auto_20180106_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleplan',
            name='meal_id',
        ),
        migrations.AddField(
            model_name='singleplan',
            name='meal_id',
            field=models.ManyToManyField(to='Meals.Meals'),
        ),
    ]
