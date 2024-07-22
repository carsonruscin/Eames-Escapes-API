from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100)