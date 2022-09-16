from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course, Student
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })

def course(request, course_code):
    course = Course.objects.get(code=course_code)
    return render(request, "courses/course.html", {
        "course": course,
        "students": course.student.all(),
        "nostudents": Student.objects.exclude(students=course).all(),
    })

def book(request, course_code):
    if request.method == "POST":
        course = Course.objects.get(pk=course_code)
        student = Student.objects.get(pk=request.POST['students'])
        course.student.add(student)
        return HttpResponseRedirect(reverse('course', args=(course_code,)))

