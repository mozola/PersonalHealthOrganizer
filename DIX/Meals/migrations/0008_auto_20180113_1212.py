# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0007_components_waste'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='units',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='components',
            name='waste',
            field=models.FloatField(),
        ),
    ]
