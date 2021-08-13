from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=50)
    localname = models.PointField(srid=4326)
    objects_manager = GeoManager()

    class Meta:
        db_table = 'incident'
        verbose_name_plural = 'Incidences'

    def __str__(self):
        return self.name

class City(models.Model):
    adm1_en = models.CharField(max_length=50)
    adm1 = models.CharField(max_length=6)
    adm0_en = models.CharField(max_length=50)
    population = models.CharField(max_length=254)
    male_pop = models.CharField(max_length=254)
    female_pop = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.adm1_en


class County(models.Model):
    adm2_en = models.CharField(max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1 = models.CharField(max_length=6)
    pcode = models.CharField(max_length=9)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        db_table = 'geo_county'
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.adm2_en


class Warehouse(models.Model):
    adm2_en = models.CharField(max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1 = models.CharField(max_length=6)
    pcode = models.CharField(max_length=9)
    geom = models.PointField(srid=4326)
    
    class Meta:
        db_table = 'geo_warehouse'
        verbose_name_plural = 'Warehouse'

    def __str__(self):
        return self.pcode