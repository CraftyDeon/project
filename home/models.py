from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)