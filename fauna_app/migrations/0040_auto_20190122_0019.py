# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-21 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0039_auto_20190122_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('saved', 'for items to be purchased later'), ('merged', 'superceded by another basket'), ('open', 'currently active'), ('frozen', 'the basket cannot be modified'), ('submitted', 'has been ordered at the checkout')], default='open', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processed', 'Being processed'), ('cancel', 'Cancelled')], default='pending', max_length=10),
        ),
    ]
