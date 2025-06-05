from django.test import TestCase
from datetime import timezone
import datetime

from books.models import Book

# Create your tests here.
class BookMethodTests(TestCase):

    def test_was_published_recently_with_future_books(self): # descriptive name

        """
        was_published_recently() should return False for books
        whose publication_date is in the future.

        """ 
        future_date = datetime.datetime.now() + datetime.timedelta(days=30)
        future_book = Book(publication_date=future_date)
        self.assertFalse(future_book.was_published_recently())