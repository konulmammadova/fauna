# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-26 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0013_auto_20181225_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='visiting_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
