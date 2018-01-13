# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0003_auto_20180105_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='type',
            field=models.CharField(default=1, max_length=10, choices=[(b'sniadanie', b'sniadanie'), (b'obiad', b'obiad'), (b'kolacja', b'kolacja')]),
            preserve_default=False,
        ),
    ]
