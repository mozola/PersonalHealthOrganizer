# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPlan', '0005_auto_20180108_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sprint_id', models.IntegerField()),
                ('sprint_name', models.CharField(max_length=20)),
                ('sprint_status', models.CharField(max_length=10, choices=[(b'Nowy', b'nowy'), (b'Rozpoczety', b'rozpoczety'), (b'Skonczony', b'skonczony')])),
                ('sprint_parameters', models.ManyToManyField(to='MyPlan.SinglePlan')),
            ],
        ),
    ]
