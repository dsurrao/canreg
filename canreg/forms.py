from django.forms import ModelForm
from .models import PreliminaryQuestions

# model forms
class PreliminaryQuestionsForm(ModelForm):
    class Meta:
        model = PreliminaryQuestions
        fields = ['confirmed_diagnosis', 'history_suggests_cancer',
        'widely_metastatic_cancer', 'diagnosable_at_location',
        'treatable_at_location']






# class DSTWorkupInstitutionForm(ModelForm):
#     class Meta:
#         model = DSTWorkupInstitution
#         fields = ['institution', 'description']
#         widgets = {
#             'institution': RadioSelect
#         }
#     def __init__(self, *args, **kwargs):
#         super(DSTWorkupInstitutionForm, self).__init__(*args, **kwargs)
#         # self.fields['institution'].empty_label = 'Other'
#         self.fields['institution'].empty_label = None
