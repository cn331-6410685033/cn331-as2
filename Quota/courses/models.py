from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    seat = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name="student")

    def __str__(self):
        return f"{self.first} {self.last}"