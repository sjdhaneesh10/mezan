from django.db import models

# Create your models here.

class Masjid(models.Model):
    masjid_name = models.CharField (max_length = 100)
    masjid_address = models.TextField (max_length = 400)
    masjid_contact_no = models.CharField (max_length = 15)
    masjid_email = models.CharField (max_length = 50)
    