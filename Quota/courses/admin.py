from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "year", "semester", "max_seat", "quota")
    filter_horizontal = ("students",)

admin.site.register(Course, CourseAdmin)