# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 02:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skf', '0009_auto_20170408_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='sdate',
            field=models.DateField(default=datetime.datetime(2017, 4, 8, 2, 34, 7, 456251, tzinfo=utc)),
        ),
    ]
