# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0011_auto_20151129_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerMName',
            field=models.CharField(max_length=50, blank=True, verbose_name='Middle Name:', null=True),
        ),
    ]
