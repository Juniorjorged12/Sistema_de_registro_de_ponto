from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('listar_funcionarios'))
        self.assertEqual(response.status_code, 200)
