from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:course_code>", views.course, name="course"),
    path("<int:course_code>/book", views.book, name='book')
]