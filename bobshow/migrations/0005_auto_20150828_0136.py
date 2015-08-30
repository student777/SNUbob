# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobshow', '0004_auto_20150827_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bob',
            name='star',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
