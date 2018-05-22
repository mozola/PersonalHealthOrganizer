# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0013_auto_20180113_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='components',
            name='units',
            field=models.CharField(max_length=10, choices=[(b'sztuk', b'sztuk'), (b'kilogramy', b'kilogramy'), (b'gramy', b'gramy'), (b'litry', b'litry'), (b'litry', b'litry')]),
        ),
    ]
