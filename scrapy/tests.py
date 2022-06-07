from django.test import TestCase
from . import models


# Provide CRUD (Create, Read, Update, Delete)

# Create your tests here.
class TestModelCars(TestCase):
    """Case to test models from scrapy app Cars"""

    def test_create_model_post_success(self):
        payload = {
            "link": "Test Link",
            "title": "Test Title",
            "image": "Test image",
        }
        scrapy = models.Cars.objects.create(**payload)
        self.assertEqual(scrapy.link, payload["link"])
        self.assertEqual(scrapy.title, payload["title"])
        self.assertEqual(scrapy.image, payload["image"])

    def test_create_model_scrapy_fail(self):
        payload = {
            "link": "New Link",
            "title": "New Title",
            "image": 5,
        }
        with self.assertRaises(AttributeError):
            scrapy = models.Cars.objects.create(**payload)

    def test_update_model_scrapy(self):
        payload = {
            "link": "Toolor Kulaganda",
            "title": "Test Title",
            "image": "Test image",
        }
        # print(payload)
        new_link = "Karkira"
        scrapy = models.Cars.objects.create(**payload)
        # print(scrapy.link)
        scrapy.link = new_link
        scrapy.save()
        scrapy.refresh_from_db()
        # print(scrapy.link)
        self.assertEqual(scrapy.link, new_link)

    def test_delete_model_scrapy(self):
        payload = {
            "link": "test link",
            "title": "test title",
            "image": "test image",
        }
        scrapy = models.Cars.objects.create(**payload)
        pk = scrapy.pk
        scrapy.delete()
        with self.assertRaises(models.Cars.DoesNotExist):
            models.Cars.objects.get(pk=pk)


class TestModelAgro(TestCase):
    """Case to test models from scrapy app Agro"""

    def test_create_model_scrapy_success(self):
        payload = {
            "link": "new link",
            "title": "new title",
            "image": "image",
        }
        scrapy = models.Agro.objects.create(**payload)
        self.assertEqual(scrapy.link, payload["link"])
        self.assertEqual(scrapy.title, payload["title"])
        self.assertEqual(scrapy.image, payload["image"])

    def test_create_model_scrapy_fail(self):
        payload = {"link": "new link", "title": "test title", "image": 5}
        with self.assertRaises(AttributeError):
            scrapy = models.Agro.objects.create(**payload)

    def test_update_model_scrapy(self):
        payload = {
            "link": "Toolor Kulaganda",
            "title": "Test Title",
            "image": "Test image",
        }
        # print(payload)
        new_link = "Asman"
        scrapy = models.Agro.objects.create(**payload)
        # print(scrapy.link)
        scrapy.link = new_link
        scrapy.save()
        scrapy.refresh_from_db()
        # print(scrapy.link)
        self.assertEqual(scrapy.link, new_link)

    def test_delete_model_scrapy(self):
        payload = {
            "link": "test link",
            "title": "test title",
            "image": "test image",
        }
        scrapy = models.Agro.objects.create(**payload)
        pk = scrapy.pk
        scrapy.delete()
        with self.assertRaises(models.Agro.DoesNotExist):
            models.Agro.objects.get(pk=pk)


class TestModelEda(TestCase):
    """Case to test models from scrapy app Eda"""

    def test_create_model_scrapy_success(self):
        payload = {
            "link": "new link",
            "title": "new title",
            "image": "image",
        }
        scrapy = models.Eda.objects.create(**payload)
        self.assertEqual(scrapy.link, payload["link"])
        self.assertEqual(scrapy.title, payload["title"])
        self.assertEqual(scrapy.image, payload["image"])

    def test_create_model_scrapy_fail(self):
        payload = {"link": "new link", "title": "test title", "image": 5}
        with self.assertRaises(AttributeError):
            scrapy = models.Eda.objects.create(**payload)

    def test_update_model_scrapy(self):
        payload = {
            "link": "Toolor Kulaganda",
            "title": "Test Title",
            "image": "Test image",
        }
        # print(payload)
        new_link = "Asman"
        scrapy = models.Eda.objects.create(**payload)
        # print(scrapy.link)
        scrapy.link = new_link
        scrapy.save()
        scrapy.refresh_from_db()
        # print(scrapy.link)
        self.assertEqual(scrapy.link, new_link)

    def test_delete_model_scrapy(self):
        payload = {
            "link": "test link",
            "title": "test title",
            "image": "test image",
        }
        scrapy = models.Eda.objects.create(**payload)
        pk = scrapy.pk
        scrapy.delete()
        with self.assertRaises(models.Eda.DoesNotExist):
            models.Eda.objects.get(pk=pk)
