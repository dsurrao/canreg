
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewPatientWorkflowUI:

    workflow_url_map = {
        'NewPatientState': 'prelim_qns',
        'StageCancerState': 'stage_cancer',
        'CurativeState': 'curative',
        'PalliativeState': 'palliative'
    }

    @staticmethod
    def next_view(next_state, patient_id):
        next_view_url = NewPatientWorkflowUI.workflow_url_map[next_state]

        return HttpResponseRedirect(reverse(next_view_url, args=(patient_id,)))
