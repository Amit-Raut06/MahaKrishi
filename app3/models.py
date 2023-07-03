from django.db import models

# Create your models here.
class Fram_dt(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    stype = models.CharField(max_length=50)
    subtp= models.CharField(max_length=50)
    nextcrop = models.CharField(max_length=50)
