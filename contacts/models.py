from django.db import models

# Create your models here.

# Model for the contacts


class Contact(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.name)
