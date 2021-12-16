from django.db import models


class Country(models.Model):
    nomi = models.CharField(max_length=50)
    poytaxti = models.CharField(max_length=50)
    aholisi = models.PositiveIntegerField()