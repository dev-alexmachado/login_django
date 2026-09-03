from django.contrib.auth.models import User
from django.test import TestCase

class HomeAccessTests(TestCase):
	def test_anonymous_user_is_redirected_to_login(self):
		response = self.client.get('/home/')

		self.assertRedirects(response, '/login/?next=/home/')

	def test_authenticated_user_can_access_home(self):
		user = User.objects.create_user(
			username='usuario',
			password='senha-segura-123',
		)
		self.client.force_login(user)

		response = self.client.get('/home/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Home Page')
