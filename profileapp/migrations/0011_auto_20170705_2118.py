# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0010_auto_20170705_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestinformation',
            name='execution_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
