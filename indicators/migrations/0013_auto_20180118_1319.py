# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-18 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0012_auto_20171229_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalindicator',
            name='baseline_na',
            field=models.BooleanField(
                default=False, help_text=b' ', verbose_name=b'Not applicable'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='baseline_na',
            field=models.BooleanField(
                default=False, help_text=b' ', verbose_name=b'Not applicable'),
        ),
    ]
