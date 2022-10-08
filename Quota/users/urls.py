from django.urls import path
from . import views
from courses.views import course

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('courses/', course, name='courses'),
    path('mycourses/', views.my_courses, name='my_courses'),
    path('withdraw/<str:course_code>', views.withdraw, name='withdraw'),
]