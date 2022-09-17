from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('courses/', views.courses, name='courses'),
    path('mycourses/', views.my_courses, name='my_courses'),
]