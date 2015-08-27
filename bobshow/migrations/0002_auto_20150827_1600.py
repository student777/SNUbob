# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobshow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bob',
            old_name='bob',
            new_name='place',
        ),
    ]
