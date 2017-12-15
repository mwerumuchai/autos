from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,blank=False)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)
    description = models.TextField(max_length=600)


    def save_category(self):
        self.save()

    @classmethod
    def get_category(cls):
        category = Category.objects.all()

        return category


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=150,blank=False)
    vehicle_image = models.ImageField(upload_to = 'motors-photos/',blank=False)
    vehicle_description = models.TextField(max_length=600)
    category = models.ForeignKey(Category)


    @classmethod
    def get_vehicles(cls):
        vehicles = Vehicle.objects.all()

        return vehicles

    @classmethod
    def get_single_vehicle(cls, pk):
        vehicles = cls.objects.get(pk=pk)
        return vehicles

    @property
    def image_url(self):
        if self.vehicle_image and hasattr(self.vehicle_image, 'url'):
            return self.vehicle_image.url

    @classmethod
    def search_by_title(cls,search_term):
        vehicles = cls.objects.filter(vehicle_name__icontains=search_term)
        return vehicles


    def __str__(self):
        return self.vehicle_name



class VehicleDetails(models.Model):
    name = models.ForeignKey(Category)
    manufacturer = models.CharField(max_length=150, blank=False)
    model = models.CharField(max_length=150, blank=False)
    color = models.CharField(max_length=100,blank=False)
    no_of_seats = models.IntegerField(blank=False)
    engine = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)
    vehicle = models.ForeignKey(Vehicle)


    @classmethod
    def get_vehicles_details(cls):
        vehicles = Vehicle.objects.all()

        return vehicles

    @classmethod
    def get_single_vehicle_details(cls, pk):
        vehicles = cls.objects.get(pk=pk)

        return vehicles

    def __str__(self):
        return self.model
