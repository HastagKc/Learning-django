from django.db import models
from django.utils.timezone import now

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  email = models.EmailField()
  enrollement = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=now)

  def __str__(self):
      return self.name
  

