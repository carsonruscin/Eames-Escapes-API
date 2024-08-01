from django.db import models
from django.contrib.auth.models import User
from .property import Property

class Booking(models.Model):
    related_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_nights = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)