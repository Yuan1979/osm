from django.db import models

# Create your models here.

class Nodes(models.Model):
   id = models.BigIntegerField(db_column='osm_id', primary_key=True)

   class Meta:
       db_table = 'planet_osm_point' 
