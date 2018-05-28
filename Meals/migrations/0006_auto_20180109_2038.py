# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0005_components'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meals',
            name='components',
        ),
        migrations.AddField(
            model_name='meals',
            name='components',
            field=models.ManyToManyField(to='Meals.Components'),
        ),
    ]
