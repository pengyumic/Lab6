# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sel_levl',
            field=models.CharField(default="'dummy'", max_length=50),
        ),
    ]