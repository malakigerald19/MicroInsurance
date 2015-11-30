# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurApp', '0019_customeravail_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='microinsuranceusers',
            name='name',
            field=models.CharField(blank='False', max_length=120, verbose_name='Name'),
        ),
    ]
