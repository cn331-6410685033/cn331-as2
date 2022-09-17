from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course

# Create your views here.

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })

def course(request, course_code):
    course = Course.objects.get(code=course_code)
    return render(request, "courses/course.html", {
        "course": course,
        "students": course.students.all(),
        #"nostudents": User.objects.exclude(students=course).all(),
    })

def book(request, course_code):
    if request.method == "POST":
        course = Course.objects.get(pk=course_code)
        student = User.objects.get(pk=request.POST['students'])
        course.students.add(student)
        return HttpResponseRedirect(reverse('course', args=(course_code,)))

