from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    elevation = models.IntegerField()  # in meters
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
