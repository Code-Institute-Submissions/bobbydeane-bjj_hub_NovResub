from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    # Test to check that the required field are valid.

    def test_order_name_are_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())

    def test_order_email_are_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())

    def test_order_address_are_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
