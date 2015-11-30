# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0005_auto_20151129_0553'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='underwriter',
            unique_together=set([]),
        ),
    ]
