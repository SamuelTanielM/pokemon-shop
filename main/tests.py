from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        # membuat objek untuk di test
        Product.objects.create(name="Test Model", amount=10, price=50)  

    def test_model_exists(self): #mengecek jika objek yang dibuat ada
        model = Product.objects.get(name="Test Model", amount=10, price=50)
        self.assertIsNotNone(model)

    def test_model_properties(self): #mengecek jika data objek yang dibuat benar
        model = Product.objects.get(name="Test Model", amount=10, price=50)
        self.assertEqual(model.name, "Test Model")
        self.assertEqual(model.amount, 10)
        self.assertEqual(model.price, 50)