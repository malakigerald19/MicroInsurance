# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0017_auto_20151130_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='branch',
            field=models.ForeignKey(to='InsurApp.Branch', verbose_name='Branch', blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='underwriter',
            field=models.ForeignKey(to='InsurApp.UnderWriter', verbose_name='UnderWriter', blank=True, null=True, default=''),
        ),
        migrations.AlterUniqueTogether(
            name='underwriter',
            unique_together=set([('UnderWriterName', 'UnderWriterAddress', 'UnderWriterContactNo')]),
        ),
    ]
