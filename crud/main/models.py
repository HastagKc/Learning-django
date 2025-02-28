from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=20)
  email = models.EmailField()
  age = models.PositiveIntegerField()
  enrollment = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name




