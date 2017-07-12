from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import date

from .models import Patient, PreliminaryQuestions, PreliminaryQuestionsForm

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
    if request.method == 'POST':
        form = PreliminaryQuestionsForm(request.POST)
        pq = form.save(commit=False)
        pq.patient = patient
        pq.recorded_date = date.today()
        pq.save()
    else:
        form = PreliminaryQuestionsForm()

    return render(request, 'canreg/prelim_qns.html',
    {'form': form, 'patient': patient})
