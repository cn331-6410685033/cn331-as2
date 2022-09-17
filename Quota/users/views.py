from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, models

from courses.models import Course

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'users/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out'
    })

def courses(request):
    return render(request)

def my_courses(request):
    courses = Course.objects.all()
    users = models.User.objects.all()
    return render(request, 'users/my_courses.html', {
        "users":users,
        "courses":courses
    })

def withdraw(request, course_code):
    course = Course.objects.get(code=course_code)
    if request.user in course.students.all():
        course.students.remove(request.user)
        course.total_seat = course.students.count()
        if course.total_seat != course.max_seat:
            course.quota_seat = True
    course.save()
    return HttpResponseRedirect(reverse('my_courses'))