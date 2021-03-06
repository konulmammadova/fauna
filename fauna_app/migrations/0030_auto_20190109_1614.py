# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-09 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0029_auto_20190109_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
