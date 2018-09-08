# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-11 07:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.City'),
        ),
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='store',
            name='sellers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='site',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storages.Storage'),
        ),
    ]