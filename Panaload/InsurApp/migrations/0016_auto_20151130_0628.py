# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0015_auto_20151129_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='microinsuranceusers',
            name='branch',
            field=models.ForeignKey(to='InsurApp.Branch', verbose_name='Branch', default=''),
        ),
        migrations.AddField(
            model_name='microinsuranceusers',
            name='underwriter',
            field=models.ForeignKey(to='InsurApp.UnderWriter', verbose_name='UnderWriter', default=''),
        ),
    ]
