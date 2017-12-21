from django.test import TestCase, Client
from django.urls import reverse

class TestTripmeBotView(TestCase):
	def setUp(self):
		self.url = reverse('chatbot:tripme')
		self.client = Client()

	def test_get(self):
		response = self.client.get(self.url)
		print(response.content)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b"Error, invalid token")

		