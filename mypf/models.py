from django.db import models

# Create your models here.

# Creating Contact Model
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email