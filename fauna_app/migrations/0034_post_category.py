# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-13 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0033_auto_20190114_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fauna_app.Category'),
        ),
    ]
