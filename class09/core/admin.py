from django.contrib import admin
from .models import Student

# Register your models here.


# admin.site.register(Student)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'roll', 'name', 'address', 'email')
    search_fields = ('id', 'roll')
