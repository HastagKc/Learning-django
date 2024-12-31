from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name
