from django.db import models

# Create your models here.
class Registration(models.Model):
  roll = models.IntegerField()
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  email = models.EmailField()
  password = models.CharField(max_length=200)

  def __str__(self):
    return str(self.roll)



