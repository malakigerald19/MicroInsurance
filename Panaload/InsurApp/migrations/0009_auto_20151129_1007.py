# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0008_auto_20151129_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAvail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('CustomerFName', models.CharField(max_length=50, verbose_name='First Name:')),
                ('CustomerMname', models.CharField(max_length=50, verbose_name='Middle Name:')),
                ('CustomerLName', models.CharField(max_length=50, verbose_name='Last Name:')),
                ('CustomerContactNo', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639|)\\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")], verbose_name='Contact No:,', default='')),
                ('InsuranceApplied', models.ForeignKey(to='InsurApp.Insurance', verbose_name='Insurance Applied:', default='')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name_plural': 'Customer Info and Insurances',
            },
        ),
        migrations.AlterUniqueTogether(
            name='customeravail',
            unique_together=set([('CustomerFName', 'CustomerMname', 'CustomerLName', 'InsuranceApplied')]),
        ),
    ]
