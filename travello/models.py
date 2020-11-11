from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
