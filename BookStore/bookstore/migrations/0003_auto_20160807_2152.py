# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20160804_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.CharField(max_length=200),
        ),
    ]
