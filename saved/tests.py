from django.test import TestCase

# Simple test to check page exists
def test_Saved_get(self):
    resp = self.client.get(reverse('saved:saved'))
    self.assertEqual(resp.status_code, 302)
    self.assertRedirects(resp, "/saved/")
