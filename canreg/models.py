from django.db import models

# dictionary tables start

# Female, Male, Other
class GenderDict(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class InstitutionDict(models.Model):
    name = models.CharField(max_length=50)
    is_predefined = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

# dictionary tables end

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class User(Person):
    username = models.CharField(max_length=20, unique=True)

class Patient(models.Model):
    gender = models.ForeignKey(GenderDict, on_delete=models.CASCADE)
    mrn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True)
    year_of_birth = models.PositiveIntegerField()
    travel_time = models.CharField(max_length=20, blank=True)
    travel_method = models.CharField(max_length=30, blank=True)
    travel_cost = models.CharField(max_length=20, blank=True)
    photo_url = models.CharField(max_length=300, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name

class PatientAddress(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    line_1 = models.CharField(max_length=200)
    line_2 = models.CharField(max_length=200)
    line_3 = models.CharField(max_length=200)
    def __str__(self):
        return self.line_1

class PatientPhone(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    cell_phone_number = models.CharField(max_length=20)
    cell_phone_contact_name = models.CharField(max_length=50)
    permission_to_call = models.BooleanField(default=False)
    permission_to_text = models.BooleanField(default=False)
    ordinal = models.IntegerField()
    def __str__(self):
        return self.cell_phone_number

class PreliminaryQuestions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    confirmed_diagnosis = models.BooleanField()
    history_suggests_cancer = models.NullBooleanField()
    widely_metastatic_cancer = models.BooleanField()
    diagnosable_at_location = models.BooleanField()
    treatable_at_location = models.NullBooleanField()
    recorded_date = models.DateTimeField(auto_now=True)

class PatientWorkflowHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    workflow_state = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
