from django.forms import ModelForm, modelformset_factory, RadioSelect,\
CheckboxSelectMultiple, CheckboxInput, Textarea, SplitDateTimeWidget, \
SelectDateWidget

from .models import BiopsyStatusDict, BiopsyTypeDict,\
BiopsyHistologyDict, AnatomySiteDict, AnatomyLocationDict, AnatomyBoneDict,\
ReceptorStrengthDict, ReceptorTestDict, NoBiopsyReasonDict, Biopsy, BiopsySite,\
BiopsyReceptorStatus, ScheduledBiopsy, Pathology

class PathologyForm(ModelForm):
    class Meta:
        model = Pathology
        fields = ['biopsy_status', 'no_biopsy_reason']
        widgets = {
            'biopsy_status': RadioSelect(),
            'no_biopsy_reason': RadioSelect()
        }
    def __init__(self, *args, **kwargs):
        super(PathologyForm, self).__init__(*args, **kwargs)
        self.fields['biopsy_status'].empty_label = None
        self.fields['no_biopsy_reason'].empty_label = None

class BiopsyForm(ModelForm):
    class Meta:
        model = Biopsy
        fields = ['pathologist_facility', 'pathologist_name',
        'type','histology', 'grade', 'procedure_date', 'pathology_report_date',
        'lvi']
        widgets = {
            'procedure_date': SelectDateWidget,
            'pathology_report_date': SelectDateWidget,
            'lvi': RadioSelect,
            'grade': RadioSelect,
            'histology': RadioSelect,
            'type': RadioSelect,
            'pathologist_facility': RadioSelect
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
        fields = ['site', 'location', 'bone', 'side']
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

class BiopsyReceptorStatusForm(ModelForm):
    class Meta:
        model = BiopsyReceptorStatus
        fields = ['receptor', 'strength', 'test_name', 'is_positive']
        widgets = {
            'strength': RadioSelect,
            'test_name': RadioSelect
        }
        def __init__(self, *args, **kwargs):
            super(BiopsyReceptorStatusForm, self).__init__(*args, **kwargs)
            self.fields['receptor'].empty_label = None
            self.fields['strength'].empty_label = None
            self.fields['test_name'].empty_label = None
