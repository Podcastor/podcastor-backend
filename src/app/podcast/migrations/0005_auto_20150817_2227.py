# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_auto_20150817_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
    ]
