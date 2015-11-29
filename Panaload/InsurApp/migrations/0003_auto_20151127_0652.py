# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0002_auto_20151127_0642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterModelOptions(
            name='insurance',
            options={'ordering': ('id',), 'verbose_name_plural': 'Insurances'},
        ),
        migrations.AddField(
            model_name='employee',
            name='EmployeeStatus',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=10, default='Active', verbose_name='Status:'),
        ),
        migrations.AddField(
            model_name='employee',
            name='EmployeeType',
            field=models.CharField(choices=[('M', 'Manager'), ('R', 'Regular')], max_length=50, default='Active'),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='UnderWriterStatus',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=10, default='Active', verbose_name='Status'),
        ),
    ]
