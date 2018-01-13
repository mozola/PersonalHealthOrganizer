# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyPlan', '0006_sprints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleplan',
            name='plan_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
