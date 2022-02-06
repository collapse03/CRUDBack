from django.db import models

class Empresa (models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    nit = models.CharField(max_length=250)
    phone = models.BigIntegerField()