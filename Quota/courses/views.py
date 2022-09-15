from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })

def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, "courses/course.html", {
        "course": course,
    })
