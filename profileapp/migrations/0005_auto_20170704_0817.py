# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_requestinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ip_address',
            field=models.GenericIPAddressField(default=None),
        ),
    ]
