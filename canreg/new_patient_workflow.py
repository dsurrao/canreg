from .models import Patient, PreliminaryQuestions, DSTWorkup, \
PatientWorkflowHistory

class NewPatientWorkflow:
    def __init__(self, patient):
        self.patient = patient

    def get_workflow_state():
        label = ''


    def save_workflow_state(workflow_state, is_complete):
        # add logic here to save to PatientWorkflowHistory model
        # ...
        save_workflow_history = staticmethod(save_workflow_history)


class NewPatientState:
    label = 'NewPatientState'

    def __init__(self, patient):
        self.patient = patient

    def start_workflow_state(self):
        NewPatientWorkflow.save_workflow_history(self.patient, self.label,
        false)

    def get_next_workflow_state(self):
        return StageCancerState(patient)

    def is_complete(self):
        try:
            pq = PreliminaryQuestions.objects.filter(
            patient__mrn=self.patient.mrn).order_by('-recorded_date')[0]

        except DoesNotExist:
            # ...
            i = 0

class StageCancerState:
    label = 'StageCancerState'

    def __init__(self, patient):
        self.patient = patient

    def start_workflow_state(self):
        NewPatientWorkflow.save_workflow_history(self.patient, self.label,
        false)

    def get_next_workflow_state(self):
        return AdmitPatientStage(patient)

    def is_complete(self):
        i = 0
