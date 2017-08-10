# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import modelformset_factory, inlineformset_factory, \
    RadioSelect, NullBooleanSelect
from canreg.models import Patient
from .models import Pathology, Receptor, BiopsyReceptorStatus, Biopsy, \
    BiopsySite, ScheduledBiopsy
from .forms import BiopsyStatusForm, NoBiopsyForm, BiopsyForm, BiopsySiteForm, \
    ScheduledBiopsyForm

# Create your views here.
def biopsy_status(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    try:
        pathology = Pathology.objects.get(patient__id=patient_id)
    except Pathology.DoesNotExist:
        pathology = Pathology(patient=patient)
    if request.method == 'POST':
        form = BiopsyStatusForm(request.POST, instance=pathology)
        form.save()
        form.is_valid()
        if form.cleaned_data['biopsy_status'].name == 'Completed':
            return HttpResponseRedirect(reverse('biopsy', args=(pathology.id,)))
        elif form.cleaned_data['biopsy_status'].name == 'Scheduled':
            return HttpResponseRedirect(reverse('scheduled_biopsy',
                args=(pathology.id,)))
        else:
            return HttpResponseRedirect(reverse('no_biopsy',
                args=(pathology.id,)))
    else:
        form = BiopsyStatusForm(instance=pathology)
    return render(request, 'canreg/biopsy_status.html',
        {'form':form, 'patient':patient})


def biopsy(request, pathology_id):
    pathology = Pathology.objects.get(id=pathology_id)
    patient = Patient.objects.get(id=pathology.patient.id)
    try:
        biopsy = Biopsy.objects.get(pathology__id=pathology_id)
    except Biopsy.DoesNotExist:
        biopsy = Biopsy(pathology=pathology)

    if request.method == 'POST':
        biopsy_form = BiopsyForm(request.POST, instance=biopsy)
        biopsy_form.save()
        try:
            biopsy_site = BiopsySite.objects.get(biopsy__id=biopsy.id)
        except BiopsySite.DoesNotExist:
            biopsy_site = BiopsySite(biopsy=biopsy)

        biopsy_site_form = BiopsySiteForm(request.POST, instance=biopsy_site)
        biopsy_site_form.save()
    else:
        biopsy_form = BiopsyForm(instance=biopsy)
        try:
            biopsy_site = BiopsySite.objects.get(biopsy__id=biopsy.id)
        except BiopsySite.DoesNotExist:
            biopsy_site = BiopsySite(biopsy=biopsy)
        biopsy_site_form = BiopsySiteForm(instance=biopsy_site)

    StatusFormset = inlineformset_factory(Biopsy, BiopsyReceptorStatus,
        fields=('receptor', 'strength', 'test_name', 'is_positive'),
        max_num = 3,
        widgets={
            'is_positive': NullBooleanSelect
        })
    if request.method == 'POST':
        formset = StatusFormset(request.POST, instance=biopsy)
        if formset.is_valid():
            formset.save()
    else:
        formset = StatusFormset(instance=biopsy)

    if request.method == 'POST':
        return HttpResponseRedirect(reverse('patients'))

    return render(request, 'canreg/biopsy.html',
        {'biopsy_form': biopsy_form,
        'biopsy_site_form': biopsy_site_form,
        'biopsy_receptor_status_formset': formset,
        'patient': patient,
        'pathology_id': pathology.id})

def no_biopsy(request, pathology_id):
    pathology = Pathology.objects.get(id=pathology_id)
    patient = Patient.objects.get(id=pathology.patient.id)

    if request.method == 'POST':
        form = NoBiopsyForm(request.POST, instance=pathology)
        form.save()
        return HttpResponseRedirect(reverse('patients'))
    else:
        form = NoBiopsyForm(instance=pathology)

    return render(request, 'canreg/no_biopsy.html',
        {'form':form, 'patient': patient, 'pathology_id':pathology.id})

def scheduled_biopsy(request, pathology_id):
    pathology = Pathology.objects.get(id=pathology_id)
    patient = Patient.objects.get(id=pathology.patient.id)

    try:
        scheduled_biopsy = ScheduledBiopsy.objects.get(
            pathology__id=pathology_id)
    except ScheduledBiopsy.DoesNotExist:
        scheduled_biopsy = ScheduledBiopsy(pathology=pathology)

    if request.method == 'POST':
        form = ScheduledBiopsyForm(request.POST, instance=scheduled_biopsy)
        form.save()
        return HttpResponseRedirect(reverse('patients'))
    else:
        form = ScheduledBiopsyForm(instance=scheduled_biopsy)

    return render(request, 'canreg/scheduled_biopsy.html',
        {'form':form, 'patient':patient, 'pathology_id':pathology.id})
