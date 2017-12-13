from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=30,blank=False)
    vehicle_type = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)

    def __str__(self):
        return self.name

class VehicleDetails(models.Model):
    name = models.ForeignKey(Vehicle)
    manufacturer = models.CharField(max_length=150, blank=False)
    model = models.CharField(max_length=150, blank=False)
    color = models.CharField(max_length=100,blank=False)
    no_of_seats = models.IntegerField(blank=False)
    engine = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)


    def __str__(self):
        return self.name
