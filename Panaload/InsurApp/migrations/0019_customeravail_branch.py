# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0018_auto_20151130_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeravail',
            name='branch',
            field=models.ForeignKey(to='InsurApp.Branch', null=True, default='', verbose_name='Branch', blank=True),
        ),
    ]
