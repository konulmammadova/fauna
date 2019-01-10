# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-24 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0009_auto_20181210_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('id',), 'verbose_name': 'Servis', 'verbose_name_plural': 'Servislər'},
        ),
        migrations.AddField(
            model_name='globalmodel',
            name='appointment_image',
            field=models.ImageField(blank=True, null=True, upload_to='appointment/'),
        ),
        migrations.AddField(
            model_name='globalmodel',
            name='appointment_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
