# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0006_auto_20170809_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biopsy',
            name='pathology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathology.Pathology'),
        ),
    ]
