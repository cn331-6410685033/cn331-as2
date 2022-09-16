from django.contrib import admin
from .models import Course, Student

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "year", "semester", "max_seat", "quota")

admin.site.register(Course, CourseAdmin)
admin.site.register(Student)