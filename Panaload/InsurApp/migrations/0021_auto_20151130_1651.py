# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0020_microinsuranceusers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerContactNo',
            field=models.CharField(verbose_name='Contact No', default='', max_length=13, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639|)\\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerFName',
            field=models.CharField(verbose_name='First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerLName',
            field=models.CharField(verbose_name='Last Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='customeravail',
            name='CustomerMName',
            field=models.CharField(verbose_name='Middle Name', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customeravail',
            name='timestamp',
            field=models.DateTimeField(verbose_name='Date Registered', auto_now_add=True),
        ),
    ]
