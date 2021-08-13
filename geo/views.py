from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import City, County, Warehouse
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def city_dataset(request):
    city  = serialize('geojson', City.objects.all())
    return HttpResponse(city, content_type = 'json')

# def incident_dataset(request):
#     incident  = serialize('geojson', Incident.objects.all())
#     return HttpResponse(incident, content_type = 'json')

def county_dataset(request):
    incident  = serialize('geojson', County.objects.all())
    return HttpResponse(incident, content_type = 'json')


def warehouse_dataset(request):
    incident  = serialize('geojson', Warehouse.objects.all())
    return HttpResponse(incident, content_type = 'json')