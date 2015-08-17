# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_auto_20150817_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='audio_link',
            field=models.URLField(max_length=120),
        ),
        migrations.AlterField(
            model_name='episode',
            name='link',
            field=models.URLField(max_length=120),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='link',
            field=models.URLField(max_length=120),
        ),
    ]
