# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0012_auto_20170705_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestinformation',
            name='request_method',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
