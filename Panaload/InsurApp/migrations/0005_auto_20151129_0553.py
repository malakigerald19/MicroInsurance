# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0004_auto_20151127_0700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches', 'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='microinsuranceusers',
            options={'verbose_name_plural': 'Micro Insurance Users', 'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='underwriter',
            options={'verbose_name_plural': 'Under Writers', 'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='branch',
            name='BranchStatus',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], verbose_name='Status', default='Active', max_length=10),
        ),
        migrations.AddField(
            model_name='microinsuranceusers',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], verbose_name='Status', default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='branch',
            name='BranchContactNo',
            field=models.CharField(verbose_name='Branch Contact No.:', default='', max_length=13, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639|)\\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceAgeMax',
            field=models.IntegerField(verbose_name='Maximum Age:'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceAgeMin',
            field=models.IntegerField(verbose_name='Minimum Age:', validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(115)]),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceAmount',
            field=models.DecimalField(verbose_name='Insured Amount:', decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceBasePrice',
            field=models.DecimalField(verbose_name='Insurance Base Price:', decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceLimit',
            field=models.IntegerField(verbose_name='Limit Per Person:'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceSellingPrice',
            field=models.DecimalField(verbose_name='Insurance Selling Price:', decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='InsuranceValidity',
            field=models.IntegerField(verbose_name='Insurance Validity(days):'),
        ),
        migrations.AlterField(
            model_name='microinsuranceusers',
            name='usertype',
            field=models.CharField(choices=[('M', 'Manager'), ('F', 'FrontLiner'), ('F', 'UnderWriter')], max_length=120),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='UnderWriterContactNo',
            field=models.CharField(verbose_name='UnderWriter Contact No.:', default='', max_length=14, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639|)\\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")]),
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together=set([('BranchName', 'BranchAddress', 'BranchContactNo')]),
        ),
        migrations.AlterUniqueTogether(
            name='underwriter',
            unique_together=set([('UnderWriterName', 'UnderWriterAddress', 'UnderWriterContactNo')]),
        ),
        migrations.RemoveField(
            model_name='branch',
            name='BranchManager',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
