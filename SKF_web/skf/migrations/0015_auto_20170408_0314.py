# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skf', '0014_auto_20170408_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=500),
        ),
    ]
