# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-07 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0002_globalmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalmodel',
            options={'verbose_name': 'Global', 'verbose_name_plural': 'Global'},
        ),
        migrations.AlterField(
            model_name='globalmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
