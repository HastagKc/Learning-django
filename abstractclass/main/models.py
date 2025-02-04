from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
  phone_number = models.CharField(max_length=100, default='')
  address = models.CharField(max_length=100, default='')

  def __str__(self):
      return self.username



