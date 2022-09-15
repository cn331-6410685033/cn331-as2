from django.contrib import admin
from .models import Course, Student

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name")

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("Courses",)

admin.site.register(Course)
admin.site.register(Student)