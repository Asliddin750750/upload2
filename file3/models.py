from django.db import models


class Notebook(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='notebooks/')

