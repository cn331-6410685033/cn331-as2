from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ssl import AlertDescription
from .models import Course

# Create your views here.

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })

def all_courses(request):
    return render(request, "courses/all_courses.html", {
        "courses": Course.objects.all()
    })

def course(request, course_code):
    course = Course.objects.get(code=course_code)
    return render(request, "courses/course.html", {
        "course": course,
        "students": course.students.all(),
    })

def enroll(request, course_code):
    course = Course.objects.get(code=course_code)
    if (course.quota) and (course.quota_seat):
        course.students.add(request.user)
        course.total_seat = course.students.count()
        if course.total_seat == course.max_seat:
            course.quota_seat = False
        course.save()
    return HttpResponseRedirect(reverse('my_courses'))
