from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['id', 'name','email','age','enrollment','created_at']


# admin.site.register(Student)