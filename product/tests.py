from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductSearchAPITestCase(TestCase):
    # @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            title='Earphone',
            description='Simple and easy to carry',
            selling_price=50,
            market_price=80,
            category='Electronics',
            images='earphone.jpg'
        )
        Product.objects.create(
            title='T-shirt',
            description='Black Slim offshoulder',
            selling_price=70,
            market_price=90,
            category='Clothing',
            images='t-shirt.jpg'
        )

    def test_search_by_title(self):
        response = self.client.get(reverse('product_search'), {'title': 'Earphone'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Earphone')
        self.assertNotContains(response, 'T-shirt')

    def test_search_by_description(self):
        response = self.client.get(reverse('product_search'), {'description': 'Black Slim offshoulder'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Earphone')
        self.assertContains(response, 'T-shirt')

    def test_search_by_category(self):
        response = self.client.get(reverse('product_search'), {'category': 'Electronics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Earphone')
        self.assertNotContains(response, 'T-shirt')

    
