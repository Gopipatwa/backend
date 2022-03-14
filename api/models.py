from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="Products", blank=True)

class Users(AbstractUser):
    contact = models.CharField(max_length=10)

    # def __str__(self):
    #     return str(self.username)+str(self.email)