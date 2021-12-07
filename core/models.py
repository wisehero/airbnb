from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    created = models.DataTimeField()
    updated = models.DataTimeField()

    class Meta:
        abstract = True
