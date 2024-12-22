from django.contrib import admin
from .models import UserTable, ProfileTable, TeacherTable, Student, Course, StudentOne

# Register your models here.


@admin.register(UserTable)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email']


@admin.register(ProfileTable)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'dob']


@admin.register(TeacherTable)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'name', 'phone']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']


@admin.register(StudentOne)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'phone']
