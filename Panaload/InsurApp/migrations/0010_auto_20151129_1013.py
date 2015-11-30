# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0009_auto_20151129_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeravail',
            old_name='CustomerMname',
            new_name='CustomerMName',
        ),
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerContactNo',
            field=models.CharField(max_length=13, default='', validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.", regex='^(09|\\+639|)\\d{9}$')], verbose_name='Contact No:'),
        ),
        migrations.AlterUniqueTogether(
            name='customeravail',
            unique_together=set([('CustomerFName', 'CustomerMName', 'CustomerLName', 'InsuranceApplied')]),
        ),
    ]
