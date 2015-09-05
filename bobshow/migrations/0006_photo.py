# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bobshow.utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bobshow', '0005_auto_20150828_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to=bobshow.utils.random_name_upload_to, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('bob', models.ForeignKey(to='bobshow.Bob')),
            ],
        ),
    ]
