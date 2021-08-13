from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(category, on_delete=PROTECT)
    brand = models.ForeignKey(brand, on_delete=CASCADE)


class review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product = models.ForeignKey(product, on_delete=CASCADE)
