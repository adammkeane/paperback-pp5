from django.test import TestCase


class TestContactViews(TestCase):
    """
    Test cases for contact app
    """

    def test_contact_page(self):
        """ Test Contact Page """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
