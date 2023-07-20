from django.test import TestCase


class TestBagViews(TestCase):
    """
    Test cases for bag app
    """

    def test_bag_page(self):
        """ Test Bag Page """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
