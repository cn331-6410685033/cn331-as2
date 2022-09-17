from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_course", views.all_courses, name="all_courses"),
    path("<str:course_code>", views.course, name="course"),
    path("<str:course_code>/enroll", views.enroll, name='enroll'),
]