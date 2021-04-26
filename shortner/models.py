from django.db import models

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uniqueId = models.CharField(max_length=10)


