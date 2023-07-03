from django.db import models

# Create your models here.
class Rbewkkh(models.Model):
  groundnuts = models.CharField(max_length=32)
  maize = models.CharField(max_length=32)


class Rblwkkh(models.Model):
    turi = models.CharField(max_length=32)
    ragi = models.CharField(max_length=32)


class Mbewskh(models.Model):
    sugarcane = models.CharField(max_length=32)
    pigeonpea = models.CharField(max_length=32)


class Mblwskh(models.Model):
    chickpea = models.CharField(max_length=32)
    fenugreek = models.CharField(max_length=32)


class Dbewskh(models.Model):

    sorghum = models.CharField(max_length=32)
    safflower = models.CharField(max_length=32)

class Dblwskh(models.Model):
 chickpea = models.CharField(max_length=32)
 rabi=models.CharField(max_length=32)


class Rbewkr (models.Model):
    gram = models.CharField(max_length=32)
    raddish = models.CharField(max_length=32)
    cabbage = models.CharField(max_length=32)


class Rblwkr (models.Model):
    vatana = models.CharField(max_length=32)
    raddish = models.CharField(max_length=32)
    gram = models.CharField(max_length=32)


class Mbewsr(models.Model):
    wheat = models.CharField(max_length=32)
    sunflower = models.CharField(max_length=32)


class MbewkR(models.Model):
    tomto = models.CharField(max_length=32)
    fenugreek = models.CharField(max_length=32)
    wheat = models.CharField(max_length=32)


class Dbewsr(models.Model):
    sorghum = models.CharField(max_length=32)
    safflower = models.CharField(max_length=32)


class Dblwsr(models.Model):
    chickpea = models.CharField(max_length=32)
    onion = models.CharField(max_length=32)










