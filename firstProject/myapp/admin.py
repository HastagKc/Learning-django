from django.contrib import admin
from .models import Student

# Register your models here.

# register using decorators
# @admin.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'address']
    search_fields = ['id', 'name']


# register using  with decorators
admin.site.register(Student, StudentAdmin)
