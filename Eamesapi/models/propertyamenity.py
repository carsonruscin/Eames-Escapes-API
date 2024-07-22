from django.db import models
from .property import Property
from .amenity import Amenity

class PropertyAmenity(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)