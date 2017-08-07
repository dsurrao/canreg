from .models import Patient, PreliminaryQuestions, PatientWorkflowHistory

class SaveResult:
    pass

class NewPatientState:
    label = 'NewPatientState'

    @staticmethod
    def save(patient):
        pwh = PatientWorkflowHistory()
        pwh.patient = patient
        pwh.workflow_state = NewPatientState.label
        pwh.is_complete = True
        pwh.save()

        result = SaveResult()
        result.is_complete = True
        result.next_state = 'StageCancerState'

        return result


# class StageCancerState:
#     label = 'StageCancerState'
#
#     @staticmethod
#     def save(patient):
#         dst = Null
#         dsts = DSTWorkup.Objects.filter(patient__id=patient.id)\
#         .order_by('-recorded_date')
#         if dsts.count() > 0:
#             dst = dsts[0]
#         else:
#             dst = DSTWorkup(patient=patient)
#             dst.save()
#
#         result = SaveResult()
#         result.is_complete = True
#         result.next_state = ''
#
#         return result
