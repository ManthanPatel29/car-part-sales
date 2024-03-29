from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class part_info(models.Model):
    name = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    is_new = models.BooleanField(max_length=200)
    owner_info = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)