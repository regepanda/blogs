# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_article_release_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
