# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_podcast_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='image',
            field=models.URLField(null=True, blank=True),
        ),
    ]
