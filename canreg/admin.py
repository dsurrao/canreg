from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(Reason)
admin.site.register(Institution)
admin.site.register(Diagnosis)
admin.site.register(DSTWorkup)
admin.site.register(DSTWorkupReason)
admin.site.register(DSTWorkupInstitution)
admin.site.register(DSTWorkupDiagnosis)
admin.site.register(PreliminaryQuestions)
