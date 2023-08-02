from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Business(models.Model):
    VERY_LOW = "$"
    LOW = "$$"
    MID = "$$$"
    HIGH = "$$$$"
    VERY_HIGH = "$$$$$"
    PRICE_CHOICES = [
        (VERY_LOW, 'very cheap'),
        (LOW, 'cheap'),
        (MID, 'moderate'),
        (HIGH, 'expensive'),
        (VERY_HIGH, 'very expensive'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES, default=MID)
    street_address = models.CharField(max_length=255)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=250)
    url = models.URLField(max_length=255)
    hours = models.CharField(max_length=255)


class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    stars = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)
    ordinal = models.IntegerField()
    business = models.ManyToManyField(Business)
