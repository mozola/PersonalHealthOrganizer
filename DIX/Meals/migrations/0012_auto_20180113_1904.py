# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0011_auto_20180113_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=b'/static/jpg/', upload_to=b'/Meals/static/jpg/'),
        ),
    ]
