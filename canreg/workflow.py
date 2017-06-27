from canreg.models import Patient, PreliminaryQuestions, DSTWorkup

class Workflow:
    states = []
    def __init__(self, patient):
        self.patient = patient
        self.states.append(NewPatientState(patient))
        self.states.append(StageCancerState(patient))

class NewPatientState:
    def __init__(self, patient):
        self.patient = patient
        self.preliminary_questions = PreliminaryQuestions(patient)

        def execute_transition(self):
            if self.preliminary_questions.confirmed_diagnosis:
                child_state = new StageCancerState()
            return child_state

class StageCancerState:
    def __init__(self, patient, dst_workup):
        self.patient = patient
        self.dst_workup = DSTWorkup(patient)
