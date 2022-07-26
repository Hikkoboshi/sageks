from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=16)
    firstname = models.CharField()
    lastname = models.CharField()
    email = models.CharField()
    phone = models.IntegerField()
    password = models.CharField()

    def __str__(self):
        return self.username
