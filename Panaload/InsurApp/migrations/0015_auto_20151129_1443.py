# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0014_auto_20151129_1400'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customeravail',
            unique_together=set([]),
        ),
    ]
