# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20150817_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='site_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
