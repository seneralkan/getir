import os
from django.contrib.gis.utils import LayerMapping
from .models import City, County, Warehouse

# To load the data to the db
# We need to enter the  shell to load the layers

#python manage.py shell
#>> from geo import load_layer
#>> load_layer.run()

city_mapping = {
    'adm1_en': 'adm1_en',
    'adm1': 'adm1',
    'adm0_en': 'adm0_en',
    'population': 'population',
    'male_pop': 'male_pop',
    'female_pop': 'female_pop',
    'geom': 'MULTIPOLYGON',
}

county_mapping = {
    'adm2_en': 'adm2_en',
    'adm1_en': 'adm1_en',
    'adm1': 'adm1',
    'pcode': 'pcode',
    'geom': 'MULTIPOLYGON',
}


warehouse_mapping = {
    'adm2_en': 'adm2_en',
    'adm1_en': 'adm1_en',
    'adm1': 'adm1',
    'pcode': 'pcode',
    'geom': 'POINT',
}

city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tr_city.shp'))
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tr_county.shp'))
warehouse_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tr_warehouse.shp'))


def run(verbose=True):
    lm = LayerMapping(City, city_shp, city_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)
    

def run_county(verbose=True):
    lm_county = LayerMapping(County, county_shp, county_mapping, transform=False, encoding='utf-8')
    lm_county.save(strict=True, verbose=verbose)

def run_wh(verbose=True):
    lm_wh = LayerMapping(Warehouse, warehouse_shp, warehouse_mapping, transform=False, encoding='utf-8')
    lm_wh.save(strict=True, verbose=verbose)