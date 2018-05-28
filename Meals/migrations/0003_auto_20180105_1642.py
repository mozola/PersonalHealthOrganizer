# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0002_meals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='components',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='meals',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=b'Meals/static/meals/image', upload_to=b'Meals/static/meals/image'),
        ),
        migrations.AlterField(
            model_name='meals',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
