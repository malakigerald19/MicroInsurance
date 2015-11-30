# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0012_auto_20151129_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeravail',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 13, 40, 11, 795179, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeravail',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
