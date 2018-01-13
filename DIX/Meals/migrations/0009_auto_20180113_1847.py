# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0008_auto_20180113_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=b'Meals/static/meals/image', upload_to=b'/home/janko/Django_Projects/DIX_V/DIX/static/meals/image'),
        ),
    ]
