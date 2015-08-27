# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobshow', '0003_bob_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='bob',
            name='score',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bob',
            name='star',
            field=models.IntegerField(),
        ),
    ]
