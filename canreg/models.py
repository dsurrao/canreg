from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Reason(models.Model):
    description = models.CharField(max_length=200)

class Institution(models.Model):
    description = models.CharField(max_length=50)

class Diagnosis(models.Model):
    description = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

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

class DSTWorkup(models.Model):
    follow_up_reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    pathology_report_institution = models.ForeignKey(Institution,
    on_delete=models.CASCADE)
    pathology_diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    imaging_studies = models.ManyToManyField(ImagingStudy)

    other_results_detail = models.CharField(max_length=200)
    no_pathology = models.BooleanField()
    pathology_report_date = models.DateTimeField('pathology report date')
    RECEPTOR_CHOICES = (
        ('Estrogen receptor', (
                ('er+', 'ER+'), ('er-', 'ER-'), ('not determined', 'not determined')
            )
        ),
        ('Progesterone receptor', (
                ('pr+', 'PR+'), ('pr-', 'PR-'), ('not determined', 'not determined')
            )
        ),
        ('HER2 IHC', (
                ('her2 ihc+', 'HER2 IHC+'), ('her2 ihc-', 'HER2 IHC-'),
                ('not determined', 'not determined')
            )
        ),
        ('HER2 FISH', (
                ('her2 fish+', 'HER2 FISH+'), ('her2 fish-', 'HER2 FISH-'),
                ('not determined', 'not determined')
            )
        )
    )
    receptor_test = models.CharField(max_length=20, choices=RECEPTOR_CHOICES)
    imaging_assessment = models.CharField(max_length=1000)
    recorded_date = models.DateTimeField('date recorded')
