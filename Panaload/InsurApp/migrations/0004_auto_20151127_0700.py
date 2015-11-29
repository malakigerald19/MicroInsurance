# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0003_auto_20151127_0652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='underwriter',
            options={'verbose_name_plural': 'Under Writers'},
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='UnderWriterContactNo',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^(09|\\+639|)\\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")], default='', max_length=13, verbose_name='UnderWriter Contact No.:'),
        ),
    ]
