from django.db import models
from .models import Institution, Receptor, Person, Patient

# dictionary tables begin
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

class NoBiopsyReasonDict(models.Model):
    description = models.CharField(max_length=200)
    is_predefined = models.BooleanField(default=False)
    def __str__(self):
        return self.description

# dictionary tables end

class Biopsy(models.Model):
    pathologist_facility = models.ForeignKey(Institution,
    on_delete=models.CASCADE)
    pathologist_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.ForeignKey(BiopsyTypeDict, on_delete=models.CASCADE)
    histology = models.ForeignKey(BiopsyHistologyDict, on_delete=models.CASCADE)
    grade = models.ForeignKey(BiopsyGradeDict, on_delete=models.CASCADE)

    procedure_date = models.DateTimeField()
    pathology_report_date = models.DateTimeField()
    is_lvi_positive = models.NullBooleanField()

class BiopsySite(models.Model):
    biopsy = models.ForeignKey(Biopsy, on_delete=models.CASCADE)
    site = models.ForeignKey(AnatomySiteDict, on_delete=models.CASCADE)
    location = models.ForeignKey(AnatomyLocationDict, on_delete=models.CASCADE,
    blank=True)
    bone = models.ForeignKey(AnatomyBoneDict, on_delete=models.CASCADE,
    blank=True)
    SIDE = (
        ('R', 'Right'),
        ('L', 'Left')
    )
    side = models.CharField(max_length=1, choices=SIDE)

class BiopsyReceptorStatus(models.Model):
    biopsy = models.ForeignKey(Biopsy, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    strength = models.ForeignKey(ReceptorStrengthDict, on_delete=models.CASCADE,
    blank=True)
    test_name = models.ForeignKey(ReceptorTestDict, on_delete=models.CASCADE,
    blank=True)
    is_positive = models.BooleanField(default=False)

class ScheduledBiopsy(models.Model):
    facility = models.ForeignKey(Institution, on_delete=models.CASCADE)
    type = models.ForeignKey(BiopsyTypeDict, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    planned_procedure_date = models.DateTimeField()

class Pathology(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    biopsy_status = models.ForeignKey(BiopsyStatusDict, on_delete=models.CASCADE)
    biopsy = models.ForeignKey(Biopsy, on_delete=models.CASCADE, blank=True)
    scheduled_biopsy = models.ForeignKey(ScheduledBiopsy,
    on_delete=models.CASCADE, blank=True)
    no_biopsy_reason = models.ForeignKey(NoBiopsyReason,
    on_delete=models.CASCADE, blank=True)
    recorded_date = models.DateTimeField(auto_now=True)
