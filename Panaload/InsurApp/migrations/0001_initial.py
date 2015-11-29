# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import InsurApp.models
from decimal import Decimal
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('BranchName', models.CharField(verbose_name='Branch Name:', max_length=200)),
                ('BranchAddress', models.CharField(default='', verbose_name='Branch Address:', max_length=1000)),
                ('BranchContactNo', models.CharField(default='', verbose_name='Branch Contact No.:', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('EmployeeName', models.CharField(max_length=200)),
                ('EmployeeContactNo', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('InsuranceSKU', models.CharField(verbose_name='Insurance Name:', max_length=200)),
                ('InsuranceBasePrice', models.DecimalField(default=Decimal('0'), verbose_name='Insurance Base Price:', decimal_places=2, max_digits=10)),
                ('InsuranceSellingPrice', models.DecimalField(default=Decimal('0'), verbose_name='Insurance Selling Price', decimal_places=2, max_digits=10)),
                ('InsuranceValidity', models.IntegerField(default='7', verbose_name='Insurance Validity(days):')),
                ('InsuranceAgeMin', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(115)], default='18', verbose_name='Minimum Age:')),
                ('InsuranceAgeMax', models.IntegerField(default='100', verbose_name='Maximum Age:')),
                ('InsuranceLimit', models.IntegerField(default='3', verbose_name='Limit Per Person:')),
                ('InsuranceEffectiveFrom', models.DateField(default=datetime.date.today, verbose_name='Valid From:')),
                ('InsuranceEffectiveTo', models.DateField(default=InsurApp.models.Insurance.get_deadline, verbose_name='Valid To:')),
            ],
            options={
                'verbose_name': 'Insurance',
                'verbose_name_plural': 'Insurances',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MicroInsuranceUsers',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('usertype', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('UnderWriterName', models.CharField(verbose_name='Underwriter Name:', max_length=200)),
                ('UnderWriterAddress', models.CharField(default='', verbose_name='Underwriter Address:', max_length=500)),
                ('UnderWriterContactNo', models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^(09|\\+639|)\\d{9}$')], default='', max_length=13, verbose_name='UnderWriter Contact No.:')),
            ],
        ),
        migrations.AddField(
            model_name='insurance',
            name='UnderWriter',
            field=models.ForeignKey(default='', to='InsurApp.UnderWriter'),
        ),
        migrations.AddField(
            model_name='branch',
            name='BranchManager',
            field=models.ForeignKey(default='', to='InsurApp.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='insurance',
            unique_together=set([('InsuranceSKU', 'UnderWriter')]),
        ),
    ]
