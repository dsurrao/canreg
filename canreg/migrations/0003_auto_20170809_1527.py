# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canreg', '0002_patient_year_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='year_of_birth',
            field=models.PositiveIntegerField(),
        ),
    ]
