# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobshow', '0002_auto_20150827_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='bob',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
