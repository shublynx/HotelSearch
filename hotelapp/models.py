from django.db import models


class Amenities(models.Model):
    amenity = models.CharField(max_length=100)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.FloatField()
    amenities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to="Images/", default="Images/Noimg.jpg")


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_pics = models.ImageField(upload_to="Images/", default="Images/Noimg.jpg")
