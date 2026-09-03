from django.contrib.auth.models import User
from django.test import TestCase

class AuthenticationFlowTests(TestCase):
	def test_user_can_register(self):
		response = self.client.post('/login/cadastrar/', {
			'username': 'novo_usuario',
			'password': 'senha-segura-123',
			'confirm_password': 'senha-segura-123',
		})

		self.assertRedirects(response, '/login/')
		self.assertTrue(User.objects.filter(username='novo_usuario').exists())

	def test_user_can_login_after_registering(self):
		User.objects.create_user(username='usuario', password='senha-segura-123')

		response = self.client.post('/login/', {
			'username': 'usuario',
			'password': 'senha-segura-123',
		})

		self.assertRedirects(response, '/home/')
		self.assertTrue(response.wsgi_request.user.is_authenticated)

	def test_invalid_credentials_do_not_authenticate(self):
		User.objects.create_user(username='usuario', password='senha-segura-123')

		response = self.client.post('/login/', {
			'username': 'usuario',
			'password': 'senha-incorreta',
		})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Nome de usuário ou senha inválidos.')
		self.assertFalse(response.wsgi_request.user.is_authenticated)
