# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='image',
            field=models.URLField(null=True, blank=True),
        ),
    ]
