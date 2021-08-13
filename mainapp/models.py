from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete=CASCADE)
    merk = models.ForeignKey(brand, default="", on_delete=CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()


class review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product = models, ForeignKey(product, on_delete=CASCADE)


class supplier(models.Model):
    name = models.CharField(max_length=200)
    merk = models.ForeignKey(brand, on_delete=CASCADE, default="")
