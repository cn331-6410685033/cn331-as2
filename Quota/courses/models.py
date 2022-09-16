from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    code = models.CharField("Course Code",max_length=5)
    name = models.CharField("Course Name",max_length=64)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(default=1)
    max_seat = models.IntegerField(null=True)
    quota = models.BooleanField("Available",default=True)
    student= models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.code}: {self.name}"