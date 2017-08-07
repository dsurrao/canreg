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
        fields = ['biopsy_status', 'biopsy', 'scheduled_biopsy',
        'no_biopsy_reason']

class BiopsySiteForm(ModelForm):
    class Meta:
        model = BiopsySite
        fields = ['site', 'location', 'bone', 'side']

class BiopsyReceptorStatusForm(ModelForm):
    class Meta:
        model = BiopsyReceptorStatus
        fields = ['receptor', 'strength', 'test_name', 'is_positive']
