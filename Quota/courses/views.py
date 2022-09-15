from django.shortcuts import render
from .models import Course, Student
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all(),
        "students": Student.objects.all(),
    })

def course(request, course_code):
    course = Course.objects.get(code=course_code)
    return render(request, "courses/course.html", {
        "course": course,
    })

def enroll(request, course_code):
    if request.method == "POST":
        course = Course.objects.get(code=course_code)
        student = Student.objects.get(code=str(request.POST["student"]))
        student.courses.add(course)
        # flight.passengers.add(passenger)
        return HttpResponseRedirect(reverse("course", args=(course.code,)))