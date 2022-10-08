from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course
from courses import views

# Create your tests here.

class CoursesTestCase(TestCase):

    def setUp(self):
        #create courses
        course1 = Course.objects.create(code="CN101", name="Python", max_seat=2)

    def test_seat_available(self):
        # is_seat_available should be True
        course = Course.objects.first()

        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        # is_seat_available should be False
        student1 = User.objects.create_user(username="student1")
        student2 = User.objects.create_user(username="student2")

        course = Course.objects.first()
        course.students.add(student1)
        course.students.add(student2)
        # course.refresh_from_db()

        self.assertFalse(course.is_seat_available())

    def test_to_string(self):
        course = Course.objects.get(code="CN101")

        self.assertEqual(str(course),"CN101: Python")
