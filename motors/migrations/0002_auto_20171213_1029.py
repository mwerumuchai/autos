# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 07:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='description',
            field=models.TextField(default=datetime.datetime(2017, 12, 13, 7, 29, 25, 608674, tzinfo=utc), max_length=600),
            preserve_default=False,
        ),
    ]
