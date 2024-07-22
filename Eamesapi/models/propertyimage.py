from django.db import models
from .property import Property

class PropertyImage(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_primary = models.BooleanField(default=False)