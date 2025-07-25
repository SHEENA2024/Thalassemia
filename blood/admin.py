from django.contrib import admin
from .models import Donor, PatientRequest

admin.site.register(Donor)
admin.site.register(PatientRequest)

