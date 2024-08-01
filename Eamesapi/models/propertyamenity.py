from django.db import models
from .amenity import Amenity

class PropertyAmenity(models.Model):
    related_property = models.ForeignKey('Eamesapi.Property', on_delete=models.CASCADE, related_name='property_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)