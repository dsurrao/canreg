from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import date

from .models import Patient, PreliminaryQuestions, PreliminaryQuestionsForm
from .new_patient_workflow import NewPatientWorkflow
from .new_patient_workflow_view_map import NewPatientWorkflowViewMap

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
    current_workflow_state = 'NewPatientState'
    workflow = NewPatientWorkflow(patient)
    try:
        pq = PreliminaryQuestions.objects.get(patient__id=patient_id)
        if request.method == 'POST':
            # pre-populate form with existing object, and POST data
            form = PreliminaryQuestionsForm(request.POST, instance=pq)
            form.save()
            workflow.save_workflow_state(workflow_state, True)
            workflow_view_map.check_workflow_state(workflow)
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
            workflow.save_workflow_state(current_workflow_state, True)
            workflow_view_map.check_workflow_state(workflow)
        else:
            # new form
            form = PreliminaryQuestionsForm()

    return render(request, 'canreg/prelim_qns.html',
    {'form': form, 'patient': patient})
