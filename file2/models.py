from django.db import models


class Phone2(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='phones/')


