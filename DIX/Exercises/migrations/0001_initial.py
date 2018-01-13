# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise_name', models.CharField(max_length=100)),
                ('exercise_description', models.CharField(max_length=500)),
                ('exercise_type', models.CharField(max_length=200, choices=[(b'barki', b'barki'), (b'plecy', b'plecy'), (b'nogi', b'nogi'), (b'biceps', b'biceps')])),
            ],
        ),
    ]
