from django.test import Client, TestCase
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Course


class CoursesViewTestCase(TestCase):
    def setUp(self):
        course1 = Course.objects.create(
            code="CN101", name="Python", max_seat=2)
        student1 = User.objects.create_user(username="student1")

        course1.students.add(student1)

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        response = c.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
