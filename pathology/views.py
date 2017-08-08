# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.forms import formset_factory
from canreg.models import Patient
from .models import Receptor, BiopsyReceptorStatus
from .forms import PathologyForm, BiopsyForm, BiopsySiteForm, \
BiopsyReceptorStatusForm, ScheduledBiopsyForm

# Create your views here.
def pathology(request, patient_id):
    patient = Patient.objects.get(id=patient_id)

    pathology_form = PathologyForm()
    biopsy_form = BiopsyForm()
    biopsy_site_form = BiopsySiteForm()
    scheduled_biopsy_form = ScheduledBiopsyForm()

    er = Receptor.objects.get(name="ER")
    pr = Receptor.objects.get(name="PR")
    her2 = Receptor.objects.get(name="HER2")
    StatusFormset = formset_factory(BiopsyReceptorStatusForm)
    formset = StatusFormset(initial=[
        {'receptor': er},
        {'receptor': pr},
        {'receptor': her2}
    ])

    return render(request, 'canreg/pathology.html',
        {'pathology_form': pathology_form,
        'biopsy_form': biopsy_form,
        'scheduled_biopsy_form': scheduled_biopsy_form,
        'biopsy_site_form': biopsy_site_form,
        'biopsy_receptor_status_formset': formset,
        'patient': patient})
