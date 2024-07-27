from django import models

class LandingPageImage(models.Model):
    image = models.ImageField(upload_to='landing_page/')