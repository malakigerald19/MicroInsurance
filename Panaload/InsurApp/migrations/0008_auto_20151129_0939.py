# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0007_auto_20151129_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='InsurancePolicy',
            field=models.TextField(verbose_name='Insurance Policy:', default=''),
        ),
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='usertype',
            field=models.CharField(max_length=120, choices=[('M', 'Manager'), ('F', 'FrontLiner'), ('U', 'UnderWriter')]),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='UnderWriterContactNo',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.", regex='^(09|\\+639|)\\d{9}$')], verbose_name='UnderWriter Contact No.:', default=''),
        ),
    ]
