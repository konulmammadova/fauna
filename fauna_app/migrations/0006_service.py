# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-10 11:50
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import fauna_app.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('fauna_app', '0005_auto_20181210_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=300, null=True)),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to=fauna_app.options.tools.get_service_bg_image)),
                ('image', models.ImageField(blank=True, null=True, upload_to=fauna_app.options.tools.get_service_image)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]