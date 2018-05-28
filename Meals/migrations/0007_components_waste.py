# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0006_auto_20180109_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='waste',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
