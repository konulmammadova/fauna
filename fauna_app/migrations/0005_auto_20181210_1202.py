# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-10 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0004_auto_20181210_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='btn_gray',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='btn_green',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]