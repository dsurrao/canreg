from .new_patient_workflow import NewPatientWorkflow

class NewPatientWorkflowViewMap:

def get_workflow_state_url(workflow_state):
    return ''

# check patient worflow state, if we have to move to the next state's view
def check_workflow_state(workflow):
    current_workflow_state = workflow.get_workflow_state()

    # redirect UI to current workflow state form
    if current_workflow_state.is_complete:
        next_workflow_state = current_workflow_state.get_next_workflow_state()
        next_workflow_state_url = get_workflow_state_url(next_workflow_state)
        return HttpResponseRedirect(reverse(next_workflow_state_url,
        args=(workflow.patient.id,)))
