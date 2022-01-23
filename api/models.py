from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name