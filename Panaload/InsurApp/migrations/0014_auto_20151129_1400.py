# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0013_auto_20151129_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeravail',
            name='InsuranceApplied',
            field=models.ForeignKey(null=True, verbose_name='Insurance Applied:', default='', to='InsurApp.Insurance'),
        ),
    ]
