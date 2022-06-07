from django.test import TestCase
from datetime import date
from . import models


class TestModel(TestCase):
    """Case to test models from book app"""

    def test_create_model_post_success(self):
        payload = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "Test Image",
            "author": "Aitmatov",
            "genre": "Western",
            "year_of_issue": 2020,
            "created_date": date.today(),
            "updated_date": date.today(),
            "age_control": 18,
        }
        book = models.Book.objects.create(**payload)
        self.assertEqual(book.title, payload["title"])
        self.assertEqual(book.description, payload["description"])
        self.assertEqual(book.image, payload["image"])
        self.assertEqual(book.author, payload["author"])
        self.assertEqual(book.genre, payload["genre"])
        self.assertEqual(book.year_of_issue, payload["year_of_issue"])
        self.assertEqual(book.created_date, payload["created_date"])
        self.assertEqual(book.updated_date, payload["updated_date"])
        self.assertEqual(book.age_control, payload["age_control"])

    def test_create_model_post_fail(self):
        payload = {
            "title": "New Title",
            "description": "description",
            "image": "Nature",
            "author": "Karnegy",
            "genre": "Drama",
            "year_of_issue": 2020,
            "created_date": date.today(),
            "updated_date": date.today(),
            "age_control": "five",
        }
        with self.assertRaises(ValueError):
            book = models.Book.objects.create(**payload)

    def test_update_model_book(self):
        payload = {
            "title": "horse with wings",
            "description": "description",
            "image": "Hors",
            "author": "Rumi",
            "genre": "Drama",
            "year_of_issue": 2020,
            "created_date": date.today(),
            "updated_date": date.today(),
            "age_control": 16,
        }
        new_title = "New Title"
        book = models.Book.objects.create(**payload)
        book.title = new_title
        book.save()
        book.refresh_from_db()
        self.assertEqual(book.title, new_title)

    def test_delete_model_book(self):
        payload = {
            "title": "horse with wings",
            "description": "description",
            "image": "Hors",
            "author": "Rumi",
            "genre": "Drama",
            "year_of_issue": 2020,
            "created_date": date.today(),
            "updated_date": date.today(),
            "age_control": 16,
        }
        book = models.Book.objects.create(**payload)
        pk = book.pk
        book.delete()
        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get(pk=pk)
