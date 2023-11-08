from django.db import models


class Address(models.Model):

    homeNo = models.CharField(max_length=10, blank=False,)
    street = models.CharField(max_length=70, blank=False,)
    postCode = models.CharField(max_length=10, blank=False,)
    city = models.CharField(max_length=70, blank=False,)
    country = models.CharField(max_length=70, blank=False,)
