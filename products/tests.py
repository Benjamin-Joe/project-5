from django.test import TestCase
from .models import Category, Product, User


class TestProductModel(TestCase):
    "Testing Product Model"
    def setUp(self):
        "Product model return title test"
        Category.objects.create(name='Test', slug='test')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='First Product',
                                            slug='first-product', price='9.99',
                                            image='IMG_20210324_205417')

    def test_products_model_entry(self):
        "Testing product model data"
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'First Product')


class TestCategoriesModel(TestCase):
    "Category Testing Class"
    def setUp(self):
        "Set Up Test"
        self.data1 = Category.objects.create(name='Test', slug='test')

    def test_category_model_entry(self):
        "Test Category model data insertion"
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry1(self):
        "Test category default name"
        data = self.data1
        self.assertEqual(str(data), 'Test')
