from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import date

import datetime
from django import forms
from django.forms import ModelForm, modelformset_factory, RadioSelect,\
CheckboxSelectMultiple, CheckboxInput, Textarea

from .models import Patient, PreliminaryQuestions, Institution
from .forms import PreliminaryQuestionsForm
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

def curative(request, patient_id):

    return render(request, 'canreg/curative.html',
    {'form': form, 'patient': patient})

def palliative(request, patient_id):

    return render(request, 'canreg/palliative.html',
    {'form': form, 'patient': patient})
