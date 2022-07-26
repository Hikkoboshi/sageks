from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    #image =

    def __str__(self):
        return self.name
