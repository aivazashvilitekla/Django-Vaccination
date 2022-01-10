from django.contrib import admin

from main.models import VaccineRegistration, Vaccines, Cities, Hospitals, Regions

# Register your models here.
admin.site.register(VaccineRegistration)
admin.site.register(Vaccines)
admin.site.register(Cities)
admin.site.register(Hospitals)
admin.site.register(Regions)