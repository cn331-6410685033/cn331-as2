from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    code = models.CharField("Course Code",max_length=5)
    name = models.CharField("Course Name",max_length=64)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(default=1)
    max_seat = models.IntegerField(null=True)
    total_seat = models.IntegerField(default=0)
    quota = models.BooleanField("Available",default=True)
    quota_seat = models.BooleanField("Seat Available",default=True)
    students= models.ManyToManyField(User, blank=True, related_name="courses")

    def __str__(self):
        return f"{self.code}: {self.name}"

    def is_seat_available(self):
        return self.students.count() < self.max_seat
