from django.db import models

# Create your models here.
# relationship
# types
# One to one
# example:
# user and profile

# user table


class UserTable(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


# Profile Table
class ProfileTable(models.Model):
    user = models.OneToOneField(
        UserTable, on_delete=models.CASCADE, null=True
    )
    bio = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.bio

# One to many
# Django -- ForeignKey
# Eample:
# Teacher and Student


class TeacherTable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    # relation
    teacher = models.ForeignKey(TeacherTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# many to many


class StudentOne(models.Model):
    name = models.CharField(max_length=258)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    student = models.ManyToManyField(StudentOne)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject
