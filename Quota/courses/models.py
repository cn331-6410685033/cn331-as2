from django.db import models

# Create your models here.

class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.first}: {self.last}"

class Course(models.Model):
    code = models.CharField("Course Code",max_length=5)
    name = models.CharField("Course Name",max_length=64)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(default=1)
    all_seat = models.IntegerField(null=True)
    quota = models.BooleanField("Available",default=True)
    student= models.ManyToManyField(Student, blank=True, related_name='students')

    def __str__(self):
        return f"{self.code}: {self.name}"