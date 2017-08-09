from django.forms import ModelForm, RadioSelect, SplitDateTimeWidget, \
SelectDateWidget

from .models import Biopsy, BiopsySite,BiopsyReceptorStatus, ScheduledBiopsy, \
Pathology

class BiopsyStatusForm(ModelForm):
    class Meta:
        model = Pathology
        fields = ['biopsy_status']
        widgets = {
            'biopsy_status': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(BiopsyStatusForm, self).__init__(*args, **kwargs)
        self.fields['biopsy_status'].empty_label = None

class NoBiopsyForm(ModelForm):
    class Meta:
        model = Pathology
        fields = ['no_biopsy_reason']
        widgets = {
            'no_biopsy_reason': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(NoBiopsyForm, self).__init__(*args, **kwargs)
        self.fields['no_biopsy_reason'].empty_label = None

class BiopsyForm(ModelForm):
    class Meta:
        model = Biopsy
        fields = ['pathologist_facility', 'pathologist_name',
        'type','histology', 'grade', 'procedure_hospital_or_clinic_name',
        'procedure_date', 'pathology_report_date', 'lvi']
        widgets = {
            'procedure_date': SelectDateWidget,
            'pathology_report_date': SelectDateWidget,
            'lvi': RadioSelect,
            'grade': RadioSelect,
            'histology': RadioSelect,
            'type': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(BiopsyForm, self).__init__(*args, **kwargs)
        self.fields['lvi'].empty_label = None
        self.fields['grade'].empty_label = None
        self.fields['histology'].empty_label = None
        self.fields['type'].empty_label = None
        self.fields['pathologist_facility'].empty_label = None

class ScheduledBiopsyForm(ModelForm):
    class Meta:
        model = ScheduledBiopsy
        fields = ['facility', 'type', 'contact_person',
        'planned_procedure_date']
        widgets = {
            'facility': RadioSelect,
            'type': RadioSelect,
            'planned_procedure_date': SelectDateWidget
        }
    def __init__(self, *args, **kwargs):
        super(ScheduledBiopsyForm, self).__init__(*args, **kwargs)
        self.fields['facility'].empty_label = None
        self.fields['type'].empty_label = None

class BiopsySiteForm(ModelForm):
    class Meta:
        model = BiopsySite
        fields = ['site', 'location', 'side', 'description']
        widgets = {
            'site': RadioSelect,
            'location': RadioSelect,
            'side': RadioSelect
        }
    def __init__(self, *args, **kwargs):
        super(BiopsySiteForm, self).__init__(*args, **kwargs)
        self.fields['side'].empty_label = None
        self.fields['site'].empty_label = None
        self.fields['location'].empty_label = None
