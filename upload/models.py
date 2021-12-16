from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    dirname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=10, default=None, null=True, blank=True)
    mimetype = models.CharField(max_length=50)

