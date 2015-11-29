# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='InsuranceAmount',
            field=models.DecimalField(verbose_name='Insured Amount:', default=Decimal('0'), max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='underwriter',
            name='UnderWriterStatus',
            field=models.CharField(verbose_name='Status', default='Active', choices=[('M', 'Active'), ('F', 'Inactive')], max_length=10),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceSellingPrice',
            field=models.DecimalField(verbose_name='Insurance Selling Price:', default=Decimal('0'), max_digits=10, decimal_places=2),
        ),
    ]
