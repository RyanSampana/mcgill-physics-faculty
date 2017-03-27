# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='office',
            field=models.CharField(default='RHB', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default='+1 514 398 phone', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='website',
            field=models.CharField(default='www.physics.mcgill.ca', max_length=200),
        ),
    ]
