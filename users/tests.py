from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_valid_user(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('welcome'))

    def test_welcome_view_accessible_after_login(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_view_inaccessible_without_login(self):
        response = self.client.get(reverse('welcome'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('welcome')}")
