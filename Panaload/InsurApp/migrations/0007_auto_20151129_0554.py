# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0006_auto_20151129_0554'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='insurance',
            unique_together=set([]),
        ),
    ]
