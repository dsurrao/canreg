from django.forms import ModelForm, modelformset_factory, RadioSelect,\
CheckboxSelectMultiple, CheckboxInput, Textarea


from .models import Patient, PreliminaryQuestions,\
Reason, Institution, ImagingStudy, Diagnosis, Receptor, \
DSTWorkup, DSTWorkupReason, DSTWorkupInstitution, DSTWorkupDiagnosis

# model forms
class PreliminaryQuestionsForm(ModelForm):
    class Meta:
        model = PreliminaryQuestions
        fields = ['confirmed_diagnosis', 'history_suggests_cancer',
        'widely_metastatic_cancer', 'diagnosable_at_location',
        'treatable_at_location']

class ReasonForm(ModelForm):
    class Meta:
        model = Reason
        fields = '__all__'

class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

class DSTWorkupForm(ModelForm):
    class Meta:
        model = DSTWorkup
        fields = ['no_pathology', 'pathology_report_date']

class DSTWorkupReasonForm(ModelForm):
    class Meta:
        model = DSTWorkupReason
        fields = ['reason', 'description']
        widgets = {
            'reason': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(DSTWorkupReasonForm, self).__init__(*args, **kwargs)
        self.fields['reason'].empty_label = None

class DSTWorkupInstitutionForm(ModelForm):
    class Meta:
        model = DSTWorkupInstitution
        fields = ['institution', 'description']
        widgets = {
            'institution': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(DSTWorkupInstitutionForm, self).__init__(*args, **kwargs)
        self.fields['institution'].empty_label = 'Other'

class DSTWorkupDiagnosisForm(ModelForm):
    class Meta:
        model = DSTWorkupDiagnosis
        fields = ['diagnosis', 'description']
        widgets = {
            'diagnosis': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(DSTWorkupDiagnosisForm, self).__init__(*args, **kwargs)
        self.fields['diagnosis'].empty_label = 'Other'

class ReceptorForm(ModelForm):
    class Meta:
        model = Receptor
        fields = '__all__'

class ImagingForm(ModelForm):
    class Meta:
        model = ImagingStudy
        fields = '__all__'
