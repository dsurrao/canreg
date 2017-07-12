from django.db import models
from django.forms import ModelForm

# models

class Patient(models.Model):
    mrn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Reason(models.Model):
    description = models.CharField(max_length=200)

class Institution(models.Model):
    description = models.CharField(max_length=50)

class Diagnosis(models.Model):
    description = models.CharField(max_length=100)

class ImagingStudy(models.Model):
    name = models.CharField(max_length=50)
    study_date = models.DateTimeField('study date')
    site = models.ForeignKey(Institution, on_delete=models.CASCADE)

class PreliminaryQuestions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    confirmed_diagnosis = models.BooleanField()
    history_suggests_cancer = models.NullBooleanField()
    widely_metastatic_cancer = models.BooleanField()
    diagnosable_at_location = models.BooleanField()
    treatable_at_location = models.NullBooleanField()
    recorded_date = models.DateTimeField('date recorded')

class Receptor(models.Model):
    name = models.CharField(max_length=30)

class ReceptorStatus(models.Model):
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)

class DSTWorkup(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pathology_report_institution = models.ForeignKey(Institution,
    on_delete=models.CASCADE)
    receptor_statuses = models.ManyToManyField(ReceptorStatus)

    no_pathology = models.BooleanField()
    pathology_report_date = models.DateTimeField('pathology report date')
    imaging_assessment = models.CharField(max_length=1000)
    recorded_date = models.DateTimeField('date recorded')

class DSTWorkupFollowupReason(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup, on_delete=models.CASCADE)
    follow_up_reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)

class DSTWorkupDiagnosis(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)

class DSTWorkupImagingStudy(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup, on_delete=models.CASCADE)
    imaging_study = models.ForeignKey(ImagingStudy, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)

class PatientWorkflowHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    workflow_state = models.CharField(max_length=25)
    date_started = models.DateTimeField()
    date_updated = models.DateTimeField()
    is_complete = models.BooleanField()


# model forms

class PreliminaryQuestionsForm(ModelForm):
    class Meta:
        model = PreliminaryQuestions
        fields = ['confirmed_diagnosis', 'history_suggests_cancer',
        'widely_metastatic_cancer', 'diagnosable_at_location',
        'treatable_at_location']
