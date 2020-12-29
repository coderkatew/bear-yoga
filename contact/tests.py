from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_required_fields(self):
        form = ContactForm({
            'name': 'John Doe',
            'email': 'bearyoga@example.com',
            'message': 'Hello, World.'})
        self.assertFalse(form.errors)

    def test_alert_invalid_form(self):
        form = ContactForm({'form': ''})
        self.assertEqual(form.errors['name'], [u'This field is required.'])
