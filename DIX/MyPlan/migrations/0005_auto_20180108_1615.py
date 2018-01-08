# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPlan', '0004_auto_20180106_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singleplan',
            old_name='meal_id',
            new_name='meals',
        ),
    ]
