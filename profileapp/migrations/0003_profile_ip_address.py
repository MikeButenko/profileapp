# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_auto_20170703_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
