# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0002_auto_20180120_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='exercise_type',
            field=models.CharField(max_length=200, choices=[(b'Barki', b'headers'), (b'Plecy', b'plecy'), (b'Uda', b'thigs'), (b'Bicepsy', b'biceps'), (b'Tricepsy', b'triceps'), (b'Brzuch', b'stomag'), (b'Klatka', b'chest'), (b'Piszczele', b'crossbones')]),
        ),
    ]
