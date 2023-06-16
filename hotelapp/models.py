from django.db import models


class Amenities(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.FloatField()
    description = models.TextField(null=True)
    amenities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to="Images/", default="Images/Noimg.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_pics = models.ImageField(upload_to="Images/", default="Images/Noimg.jpg")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
