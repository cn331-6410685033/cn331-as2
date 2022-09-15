from django.shortcuts import render
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
    })
