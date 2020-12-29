from django.test import TestCase
from .forms import RetreatForm


class TestRetreatForm(TestCase):

    def test_required_fields(self):
        form = RetreatForm({
            'name': 'Yoga Retreat',
            'date': '06/10/2021',
            'duration': '3',
            'description': 'Lovely retreat.',
            'price': '150',
            'location': 'Italy'})
        self.assertFalse(form.errors)

    def test_alert_invalid_form(self):
        form = RetreatForm({'form': ''})
        self.assertEqual(form.errors['location'], [u'This field is required.'])
