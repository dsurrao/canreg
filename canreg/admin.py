from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(Reason)
admin.site.register(Institution)
admin.site.register(Diagnosis)
admin.site.register(ImagingStudy)
admin.site.register(PreliminaryQuestions)
admin.site.register(DSTWorkup)
admin.site.register(Receptor)
admin.site.register(ReceptorStatus)
admin.site.register(DSTWorkupFollowupReason)
admin.site.register(DSTWorkupDiagnosis)
admin.site.register(DSTWorkupImagingStudy)
admin.site.register(PatientWorkflowHistory)
