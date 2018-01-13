# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='exercise_type',
            field=models.CharField(max_length=200, choices=[(b'barki', b'headers'), (b'plecy', b'plecy'), (b'Uda', b'thigs'), (b'biceps', b'biceps'), (b'Tricepsy', b'triceps'), (b'Brzuch', b'stomag'), (b'Klatka', b'chest'), (b'Piszczele', b'crossbones')]),
        ),
    ]
