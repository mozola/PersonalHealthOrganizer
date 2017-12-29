# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=b'templates/no-img.jpg', upload_to=b'templates'),
        ),
    ]
