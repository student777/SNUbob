# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobshow', '0006_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bob',
            name='star',
        ),
    ]
