from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from courses.models import Course

# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username="Earth", password="Ironman1234")
        student1 = User.objects.create_user(
            username="student1", password="Ironman1234")
        student2 = User.objects.create_user(
            username="student2", password="Ironman1234")

        course1 = Course.objects.create(code="CN101", name="Python", max_seat=1)

    def test_not_login_index(self):
        # redirects to login page
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse("login"))

    def test_login_index(self):
        # redirects to welcome page
        self.client.login(username="Earth", password="Ironman1234")

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        credentials = {'username': 'Earth', 'password': 'Ironman1234'}
        response = self.client.post(reverse("login"), credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_login(self):
        credentials = {'username': 'Earth', 'password': 'Batman4321'}
        response = self.client.post(reverse("login"), credentials, follow=True)
        messages = "".join(list(response.context['message']))
        self.assertEqual(messages, 'Invalid credentials.')

    def test_logout_view(self):
        self.client.login(username="Earth", password="Ironman1234")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        self.client.login(username="Earth", password="Ironman1234")
        response = self.client.post(reverse("logout"))

        messages = "".join(list(response.context['message']))
        self.assertEqual(messages, 'Logged out')

    def test_my_courses_page(self):
        self.client.login(username="Earth", password="Ironman1234")
        response = self.client.post(reverse("my_courses"))

        self.assertEqual(response.status_code, 200)

    def test_my_courses_context(self):
        student1 = self.client.login(username="Earth", password="Ironman1234")
        course1 = Course.objects.first()
        course1.students.add(student1)
        response = self.client.post(reverse("my_courses"))
        
        self.assertEqual(response.context['courses'].count(), 1)

    def test_withdraw(self):
        student1 = self.client.login(username="Earth", password="Ironman1234")
        course1 = Course.objects.first()
        course1.students.add(student1)
        self.client.post(reverse("withdraw", args=(course1.code,)))

        self.assertEqual(course1.students.count(), 0)