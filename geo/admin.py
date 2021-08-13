from django.contrib import admin
from .models import Incident, City
# Register your models here.
from leaflet.admin import LeafletGeoAdmin

class IncidentAdminModel(LeafletGeoAdmin):
    list_display = ['name', 'localname']

class CityModelAdmin(LeafletGeoAdmin):
    list_display = ['adm1_en', 'adm0_en', 'population']

admin.site.register(Incident, IncidentAdminModel)
admin.site.register(City, CityModelAdmin)
