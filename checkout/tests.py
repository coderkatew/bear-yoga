from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_required_fields(self):
        form = OrderForm({
            'full_name': 'Mr Test',
            'email': 'bearyoga@example.com',
            'phone_number': '012 3456789',
            'country': 'IE',
            'street_address1': '1 Test Lane',
            'town_or_city': 'Big City'})     
        self.assertFalse(form.errors)

    def test_alert_invalid_form(self):
        form = OrderForm({'form': ''})
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])