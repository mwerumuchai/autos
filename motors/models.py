from django.db import models
# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating

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
    name = models.CharField(max_length=150,blank=False)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)
    description = models.TextField(max_length=600)
    # ratings = GenericRelation(Rating, related_query_name='vehicles')

    # Vehicle.objects.filter(ratings__isnull=False).order_by('ratings__average')

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
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.name



class VehicleDetails(models.Model):
    name = models.ForeignKey(Vehicle)
    manufacturer = models.CharField(max_length=150, blank=False)
    model = models.CharField(max_length=150, blank=False)
    color = models.CharField(max_length=100,blank=False)
    no_of_seats = models.IntegerField(blank=False)
    engine = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'motors-photos/',blank=False)


    def __str__(self):
        return self.name
