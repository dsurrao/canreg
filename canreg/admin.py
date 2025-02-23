from django.contrib import admin

from .models import *
from pathology.models import *

admin.site.register(GenderDict)
admin.site.register(Patient)
admin.site.register(InstitutionDict)
admin.site.register(BiopsySite)
admin.site.register(BiopsyStatusDict)
admin.site.register(BiopsyTypeDict)
admin.site.register(BiopsyGradeDict)
admin.site.register(BiopsyHistologyDict)
admin.site.register(NoBiopsyReasonDict)
admin.site.register(AnatomySiteDict)
admin.site.register(AnatomyLocationDict)
admin.site.register(AnatomyBoneDict)
admin.site.register(Receptor)
admin.site.register(ReceptorStrengthDict)
admin.site.register(ReceptorTestDict)
