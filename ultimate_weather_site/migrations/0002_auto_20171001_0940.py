# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimate_weather_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperatures',
            name='date',
            field=models.DateField(),
        ),
    ]
