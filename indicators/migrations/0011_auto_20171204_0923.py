# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-04 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0010_auto_20170623_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collecteddata',
            name='achieved',
            field=models.DecimalField(
                decimal_places=2, max_digits=20, verbose_name=b'Achieved'),
        ),
        migrations.AlterField(
            model_name='historicalcollecteddata',
            name='achieved',
            field=models.DecimalField(
                decimal_places=2, max_digits=20, verbose_name=b'Achieved'),
        ),
    ]
