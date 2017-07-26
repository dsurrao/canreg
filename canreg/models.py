from django.db import models

# models

class Patient(models.Model):
    mrn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name

class Reason(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=50)
    is_predefined = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=100, default='')
    is_predefined = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class ImagingStudy(models.Model):
    name = models.CharField(max_length=50)
    is_predefined = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class PreliminaryQuestions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    confirmed_diagnosis = models.BooleanField()
    history_suggests_cancer = models.NullBooleanField()
    widely_metastatic_cancer = models.BooleanField()
    diagnosable_at_location = models.BooleanField()
    treatable_at_location = models.NullBooleanField()
    recorded_date = models.DateTimeField(auto_now=True)

# 'Estrogen', 'Progesterone', 'HER2 IHC', 'HER2 FISH'
class Receptor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class DSTWorkup(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    no_pathology = models.BooleanField()
    pathology_report_date = models.DateTimeField(null=True, blank=True)
    imaging_assessment = models.CharField(max_length=1000)
    recorded_date = models.DateTimeField(auto_now=True)

    def __str__(self):              # __unicode__ on Python 2
        return 'DSTWorkup {}'.format(self.id)

class DSTWorkupReason(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)

class DSTWorkupInstitution(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)

class DSTWorkupDiagnosis(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)

class DSTWorkupReceptorStatus(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    status = models.NullBooleanField()

class DSTWorkupImagingStudy(models.Model):
    dst_workup = models.ForeignKey(DSTWorkup, on_delete=models.CASCADE)
    site = models.ForeignKey(Institution, on_delete=models.CASCADE)
    study_date = models.DateTimeField('study date')

class PatientWorkflowHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    workflow_state = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
