# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from canreg.models import Institution, Person, Patient

# dictionary tables begin
# 'Estrogen', 'Progesterone', 'HER2 IHC', 'HER2 FISH'
class Receptor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class BiopsyStatusDict(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class BiopsyTypeDict(models.Model):
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class BiopsyGradeDict(models.Model):
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class BiopsyHistologyDict(models.Model):
    name = models.CharField(max_length=35)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class NoBiopsyReasonDict(models.Model):
    description = models.CharField(max_length=200)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.description

# Breast, Lymph node, Bone, other
class AnatomySiteDict(models.Model):
    name = models.CharField(max_length=20)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# Axillary, Supraclavicular, Cervical, other
class AnatomyLocationDict(models.Model):
    name = models.CharField(max_length=20)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class AnatomyBoneDict(models.Model):
    name = models.CharField(max_length=35)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# strong, moderate, weak
class ReceptorStrengthDict(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class ReceptorTestDict(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

# dictionary tables end

class BiopsySite(models.Model):
    site = models.ForeignKey(AnatomySiteDict, on_delete=models.CASCADE)
    location = models.ForeignKey(AnatomyLocationDict, on_delete=models.CASCADE,
    null=True)
    SIDE = (
        ('R', 'Right'),
        ('L', 'Left')
    )
    side = models.CharField(max_length=1, choices=SIDE, default='')
    bone = models.CharField(max_length=100)

class Biopsy(models.Model):
    procedure_date = models.DateTimeField()
    pathologist_name = models.CharField(max_length=200, blank=True)
    pathologist_facility = models.ForeignKey(Institution,
    on_delete=models.CASCADE)
    pathology_report_date = models.DateTimeField()
    type = models.ForeignKey(BiopsyTypeDict, on_delete=models.CASCADE)
    biopsy_site = models.ForeignKey(BiopsySite, on_delete=models.CASCADE)
    histology = models.ForeignKey(BiopsyHistologyDict, on_delete=models.CASCADE)
    grade = models.ForeignKey(BiopsyGradeDict, on_delete=models.CASCADE)
    LVI_STATUS = (
        ('LVI+', 'LVI+'),
        ('LVI-', 'LVI-'),
        ('ND', 'Not Determined'),
    )
    lvi = models.CharField(max_length=14, choices=LVI_STATUS, default='ND')
    #is_lvi_positive = models.NullBooleanField()

class BiopsyReceptorStatus(models.Model):
    biopsy = models.ForeignKey(Biopsy, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    strength = models.ForeignKey(ReceptorStrengthDict, on_delete=models.CASCADE,
    null=True)
    test_name = models.ForeignKey(ReceptorTestDict, on_delete=models.CASCADE,
    null=True)
    is_positive = models.BooleanField(default=False)

class ScheduledBiopsy(models.Model):
    planned_procedure_date = models.DateTimeField()
    facility = models.ForeignKey(Institution, on_delete=models.CASCADE)
    type = models.ForeignKey(BiopsyTypeDict, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=200, blank=True)

class Pathology(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    biopsy_status = models.ForeignKey(BiopsyStatusDict, on_delete=models.CASCADE)
    biopsy = models.ForeignKey(Biopsy, on_delete=models.CASCADE, null=True)
    scheduled_biopsy = models.ForeignKey(ScheduledBiopsy,
    on_delete=models.CASCADE, null=True)
    no_biopsy_reason = models.ForeignKey(NoBiopsyReasonDict,
    on_delete=models.CASCADE, null=True)
    recorded_date = models.DateTimeField(auto_now=True)
