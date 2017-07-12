# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSTWorkup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_pathology', models.BooleanField()),
                ('pathology_report_date', models.DateTimeField(verbose_name=b'pathology report date')),
                ('imaging_assessment', models.CharField(max_length=1000)),
                ('recorded_date', models.DateTimeField(verbose_name=b'date recorded')),
            ],
        ),
        migrations.CreateModel(
            name='DSTWorkupDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Diagnosis')),
                ('dst_workup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.DSTWorkup')),
            ],
        ),
        migrations.CreateModel(
            name='DSTWorkupFollowupReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500)),
                ('dst_workup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.DSTWorkup')),
            ],
        ),
        migrations.CreateModel(
            name='DSTWorkupImagingStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500)),
                ('dst_workup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.DSTWorkup')),
            ],
        ),
        migrations.CreateModel(
            name='ImagingStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('study_date', models.DateTimeField(verbose_name=b'study date')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrn', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PatientWorkflowHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_state', models.CharField(max_length=25)),
                ('date_started', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('is_complete', models.BooleanField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PreliminaryQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_diagnosis', models.BooleanField()),
                ('history_suggests_cancer', models.NullBooleanField()),
                ('widely_metastatic_cancer', models.BooleanField()),
                ('diagnosable_at_location', models.BooleanField()),
                ('treatable_at_location', models.NullBooleanField()),
                ('recorded_date', models.DateTimeField(verbose_name=b'date recorded')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ReceptorStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Receptor')),
            ],
        ),
        migrations.AddField(
            model_name='imagingstudy',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Institution'),
        ),
        migrations.AddField(
            model_name='dstworkupimagingstudy',
            name='imaging_study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.ImagingStudy'),
        ),
        migrations.AddField(
            model_name='dstworkupfollowupreason',
            name='follow_up_reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Reason'),
        ),
        migrations.AddField(
            model_name='dstworkup',
            name='pathology_report_institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Institution'),
        ),
        migrations.AddField(
            model_name='dstworkup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canreg.Patient'),
        ),
        migrations.AddField(
            model_name='dstworkup',
            name='receptor_statuses',
            field=models.ManyToManyField(to='canreg.ReceptorStatus'),
        ),
    ]
