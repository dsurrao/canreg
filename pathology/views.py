# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from canreg.models import Patient
from .forms import PathologyForm, BiopsySiteForm, \
BiopsyReceptorStatusForm

# Create your views here.
def pathology(request, patient_id):
    patient = Patient.objects.get(id=patient_id)

    pathology_form = PathologyForm()
    biopsy_site_form = BiopsySiteForm()
    biopsy_receptor_status_form = BiopsyReceptorStatusForm()

    return render(request, 'canreg/pathology.html',
        {'pathology_form': pathology_form,
        'biopsy_site_form': biopsy_site_form,
        'biopsy_receptor_status_form': biopsy_receptor_status_form,
        'patient': patient})
