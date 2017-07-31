from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import date

import datetime
from django import forms
from django.forms import ModelForm, modelformset_factory, RadioSelect,\
CheckboxSelectMultiple, CheckboxInput, Textarea


from .models import Patient, PreliminaryQuestions,\
Reason, Institution, ImagingStudy, Diagnosis, Receptor, \
DSTWorkup, DSTWorkupReason, DSTWorkupDiagnosis, DSTWorkupInstitution

from .forms import PreliminaryQuestionsForm, DSTWorkupForm, \
DSTWorkupReasonForm, DSTWorkupInstitutionForm, DSTWorkupDiagnosisForm, \
ReceptorForm, ImagingForm, ReasonForm, DiagnosisForm, InstitutionForm
from .new_patient_workflow import NewPatientState
from .new_patient_workflow_ui import NewPatientWorkflowUI

class IndexView(generic.ListView):
    template_name = 'canreg/index.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model = Patient
    template_name = 'canreg/detail.html'

class PrelimQnsDetailView(generic.DetailView):
    model = Patient
    form = PreliminaryQuestionsForm()
    template_name = 'canreg/prelim_qns.html'


def prelim_qns(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    try:
        pq = PreliminaryQuestions.objects.get(patient__id=patient_id)
        if request.method == 'POST':
            # pre-populate form with existing object, and POST data
            form = PreliminaryQuestionsForm(request.POST, instance=pq)
            form.save()
            state = NewPatientState.save(patient)

            # change view
            if state.is_complete:
                return NewPatientWorkflowUI.next_view(state.next_state,
                    patient_id)
        else:
            # pre-populate form with POST data
            form = PreliminaryQuestionsForm(instance=pq)
    except PreliminaryQuestions.DoesNotExist:
        if request.method == 'POST':
            # pre-populate form with POST data
            form = PreliminaryQuestionsForm(request.POST)
            pq = form.save(commit=False)
            pq.patient = patient
            pq.recorded_date = date.today()
            pq.save()
            state = NewPatientState.save(patient)

            # change view
            if state.is_complete:
                return NewPatientWorkflowUI.next_view(state.next_state,
                    patient_id)
        else:
            # new form
            form = PreliminaryQuestionsForm()

    return render(request, 'canreg/prelim_qns.html',
        {'form': form, 'patient': patient})

def stage_cancer(request, patient_id):
    patient = Patient.objects.get(id=patient_id)

    if request.method == 'GET':
        try:
            w = DSTWorkup.objects.get(patient__id=patient_id)
            dst_workup_form = DSTWorkupForm(instance=w)

            try:
                wr = DSTWorkupReason.objects.get(dst_workup__id=w.id)
                dst_workup_reason_form = DSTWorkupReasonForm(instance=wr)
            except DSTWorkupReason.DoesNotExist:
                dst_workup_reason_form = DSTWorkupReasonForm()

            try:
                wi = DSTWorkupInstitution.objects.get(dst_workup__id=w.id)
                dst_workup_institution_form = DSTWorkupInstitutionForm(
                instance=wi)
            except DSTWorkupInstituion.DoesNotExist:
                dst_workup_institution_form = DSTWorkupInstitutionForm()

            try:
                wd = DSTWorkupDiagnosis.objects.get(dst_workup__id=w.id)
                dst_workup_diagnosis_form = DSTWorkupDiagnosisForm(
                instance=wd)
            except DSTWorkupDiagnosis.DoesNotExist:
                dst_workup_diagnosis_form = DSTWorkupDiagnosisForm()
                
        except DSTWorkup.DoesNotExist:
            dst_workup_form = DSTWorkupForm()
            dst_workup_reason_form = DSTWorkupReasonForm()
            dst_workup_institution_form = DSTWorkupInstitutionForm()
            dst_workup_diagnosis_form = DSTWorkupDiagnosisForm()
    elif request.method == 'POST':
        try:
            w = DSTWorkup.objects.get(patient__id=patient_id)
            dst_workup_form = DSTWorkupForm(request.POST, instance=w)
            dst_workup_form.save()
        except DSTWorkup.DoesNotExist:
            dst_workup_form = DSTWorkupForm(request.POST)
            w = dst_workup_form.save(commit=False)
            w.patient = patient
            w.save()

        try:
            wr = DSTWorkupReason.objects.get(dst_workup__id=w.id)
            dst_workup_reason_form = DSTWorkupReasonForm(request.POST,
            instance=wr)
            dst_workup_reason_form.save()
        except DSTWorkupReason.DoesNotExist:
            dst_workup_reason_form = DSTWorkupReasonForm(request.POST)
            wr = dst_workup_reason_form.save(commit=False)
            wr.dst_workup = w
            wr.save()

        try:
            wi = DSTWorkupInstitution.objects.get(dst_workup__id=w.id)
            dst_workup_institution_form = DSTWorkupInstitutionForm(request.POST,
            instance=wi)
            dst_workup_institution_form.save()
        except DSTWorkupInstitution.DoesNotExist:
            dst_workup_institution_form = DSTWorkupInstitutionForm(request.POST)
            wi = dst_workup_institution_form.save(commit=False)
            wi.dst_workup = w
            wi.save()

        try:
            wd = DSTWorkupDiagnosis.objects.get(dst_workup__id=w.id)
            dst_workup_diagnosis_form = DSTWorkupDiagnosisForm(request.POST,
            instance=wd)
            dst_workup_diagnosis_form.save()
        except DSTWorkupDiagnosis.DoesNotExist:
            dst_workup_diagnosis_form = DSTWorkupDiagnosisForm(request.POST)
            wd = dst_workup_diagnosis_form.save(commit=False)
            wd.dst_workup = w
            wd.save()

    return render(request, 'canreg/stage_cancer.html',
        {'patient': patient,
        'dst_workup_form': dst_workup_form,
        'dst_workup_reason_form': dst_workup_reason_form,
        'dst_workup_institution_form': dst_workup_institution_form,
        'dst_workup_diagnosis_form': dst_workup_diagnosis_form})

def curative(request, patient_id):

    return render(request, 'canreg/curative.html',
    {'form': form, 'patient': patient})

def palliative(request, patient_id):

    return render(request, 'canreg/palliative.html',
    {'form': form, 'patient': patient})

def receptors(request, patient_id):

    return render(request, 'canreg/palliative.html',
    {'form': form, 'patient': patient})

def imaging_studies(request, patient_id):

    return render(request, 'canreg/palliative.html',
    {'form': form, 'patient': patient})
