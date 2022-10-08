from django.test import Client, TestCase
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Course


class CoursesViewTestCase(TestCase):
    def setUp(self):
        course1 = Course.objects.create(
            code="CN101", name="Python", max_seat=1)
        student1 = User.objects.create_user(
            username="student1", password="Ironman1234")
        student2 = User.objects.create_user(
            username="student2", password="Ironman1234")

    def test_index_view_status_code(self):
        # index view's status code is ok

        c = Client()
        response = c.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        # context is correctly set

        c = Client()
        response = c.get(reverse('courses'))
        self.assertEqual(response.context['courses'].count(), 1)

    # courses/all_course

    def test_allcourses_page(self):
        # all_courses page should return status code 200

        c = Client()
        response = c.get(reverse('all_courses'))
        self.assertEqual(response.status_code, 200)

    def test_allcourses_count(self):
        # all_courses view's status code is ok

        c = Client()
        response = c.get(reverse('all_courses'))
        self.assertEqual(response.context['courses'].count(), 1)

    # courses/course.code

    def test_valid_course_page(self):
        """ valid course page should return status code 200 """

        c = Client()
        course = Course.objects.first()
        response = c.get(reverse('course', args=(course.code,)))
        self.assertEqual(response.status_code, 200)

    def test_enroll_available(self):
        # now student in course is 0 (available), so after enroll student in course shold be 1

        # login
        self.client.login(username="student1", password="Ironman1234")

        course = Course.objects.first()
        self.client.post(reverse('enroll', args=(course.code,)))
        self.assertEqual(course.students.count(), 1)

    def test_enroll_unavailable(self):
        # Add student to course that make course fulled.
        self.client.login(username="student1", password="Ironman1234")
        course = Course.objects.first()
        self.client.post(reverse('enroll', args=(course.code,)))

        # now student in course is 1 (unavailable), that mean it can't enroll anymore
        # student count shold be the same (1)

        # login
        self.client.login(username="student2", password="Ironman1234")
        self.client.post(reverse('enroll', args=(course.code,)))

        self.assertEqual(course.students.count(), 1)
