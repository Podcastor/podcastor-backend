# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_auto_20150824_2256'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarked_episodes',
            field=models.ManyToManyField(to='podcast.Episode'),
        ),
        migrations.AddField(
            model_name='user',
            name='bookmarked_podcasts',
            field=models.ManyToManyField(to='podcast.Podcast'),
        ),
    ]
