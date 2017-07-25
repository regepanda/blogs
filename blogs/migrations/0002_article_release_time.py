# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='release_time',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
