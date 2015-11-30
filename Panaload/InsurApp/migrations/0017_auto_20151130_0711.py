# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0016_auto_20151130_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='branch',
            field=models.ForeignKey(default='', null=True, to='InsurApp.Branch', verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='underwriter',
            field=models.ForeignKey(default='', null=True, to='InsurApp.UnderWriter', verbose_name='UnderWriter'),
        ),
    ]
