from .views import HomePageView, city_dataset, county_dataset, warehouse_dataset
from django.conf.urls import include, url
from django.urls.conf import path

urlpatterns = [
    path('', HomePageView.as_view(), name = 'homepage'),
    path('city/', city_dataset, name='city'),
    path('county/', county_dataset, name='county'),
    path('warehouse/', warehouse_dataset, name='warehouse'),
]