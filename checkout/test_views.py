from django.test import TestCase
from .views import checkout_success


class TestViews(TestCase):
    def test_get_custom_404(self):
        response = self.client.get('/checkout_success/<order_number>')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
