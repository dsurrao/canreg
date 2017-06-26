from canreg.models import Patient

class Workflow:
    starting_state

class WorflowState:
    required_information = []
    child_states = []

    # processes business logic using required_information
    # to move patient to child_state
    def execute_transition(self):
        return child_state

class PatientWorkflowState:
    patient
    workflow_state
    provided_information = []

class WorkflowController:
    def define_workflow(self):
        return workflow

    def start_workflow(self, patient):
        return patient_workflow_state

    def get_workflow_state(self, patient):
        return patient_workflow_state
