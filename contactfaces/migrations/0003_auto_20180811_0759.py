# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-11 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactfaces', '0002_auto_20180811_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactfaces',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]