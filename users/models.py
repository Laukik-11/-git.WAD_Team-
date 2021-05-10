from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

# Custom Resident Model to overwrite the default user model


class Resident(AbstractUser):

    flatNo = models.CharField(max_length=6, blank=True, null=True)
    # Boolean field to be made True by the admin so that the resident can login
    is_verified = models.BooleanField(default=False)
    # Boolean field, if set to True makes the Resident visible in the Neighbours list
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["flatNo"]

    def __str__(self):
        return self.username


class Vehicle(models.Model):
    name = models.CharField(max_length=30, null=False)
    number = models.CharField(max_length=10)
    # Foreign Key to the related owner(Resident)
    owner = models.ForeignKey(
        Resident, on_delete=models.CASCADE, related_name="vehicles"
    )

    def __str__(self):
        return self.name


class Visitor(models.Model):

    name = models.CharField(max_length=30, null=False)
    purpose = models.TextField()
    number = models.CharField(max_length=12, null=False)
    # Foreign Key to the related Resident
    flat = models.ForeignKey(
        Resident, on_delete=models.CASCADE, related_name='visitors')
    entryTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-entryTime"]

    def __str__(self):
        return self.name
