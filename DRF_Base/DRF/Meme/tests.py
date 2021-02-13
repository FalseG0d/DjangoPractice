from django.test import TestCase

# Create your tests here.
class MemeModelTest(TestCase):
    def setUp(self):
        Meme.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            message=fake.text(),
            source=fake.url()
        )
    def test_save_model(self):
        saved_models = Meme.objects.count()
        self.assertEqual(saved_models, 2)