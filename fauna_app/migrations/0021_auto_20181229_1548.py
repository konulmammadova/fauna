# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-29 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0020_auto_20181229_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], default=False),
        ),
    ]
