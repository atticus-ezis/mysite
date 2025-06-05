from django.test import TestCase
from django.utils import timezone
from books.models import Publisher, Author, Book, Classification
from django.contrib.auth.models import User 

from django.urls import reverse


class IndexViewTests(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(
            name="test",
            address="test",
            city="test",
            state_province="test",
            country="test",
            website="test",
            )
        self.author = Author.objects.create(
            first_name="test",
            last_name="test",
            email="test@gmail.com"
            )
        self.classification = Classification.objects.create(
            code='HSG',
            name='test',
            description='kjasghdk',
        )
        self.book = Book.objects.create(
            title="test",
            publisher=self.publisher,
            publication_date=timezone.now(),
            classification = self.classification,
            )
       
        self.book.authors.add(self.author)
        self.username = 'test'
        self.password = 'Panda3957'
        self.user = User.objects.create_user(username=self.username, password=self.password)
       

    def test_index_view_with_books(self):
        self.client.login(username=self.username, password=self.password)
        """Books should be displayed if some books exist."""
        response = self.client.get(reverse("book_display"))
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.context["books"]),list(Book.objects.all()))

    def test_index_view_with_no_books(self):
        """Display appropriate message if no books exist."""
        self.client.login(username=self.username, password=self.password)
        Book.objects.all().delete()
        response = self.client.get(reverse("book_display"))
        self.assertContains(response, "No books are available.")
        self.assertListEqual(list(response.context["books"]),[])

    def test_search_author(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("search_author", query=[('query', 'test')]))
        view_result = response.context['authors'] # should be <QuerySet [<Author: test, test>]>
        expected_result = Author.objects.filter(first_name='test', last_name='test')
        self.assertEqual(list(view_result), list(expected_result))

    def test_book_details(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('book_details', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
    
class UserAuth(TestCase): 
    def setUp(self):
        self.username = 'test'
        self.password = 'Panda0378'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        response = self.client.post(reverse('login_user'), {
            "username":self.username,
            "password":self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/'))
    
    def test_logout_success(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.url, '/books/user/login/')

class AuthorCrud(TestCase):

    def test_create_user(self):
        self.username = 'test'
        self.password = 'Panda3957'
        self.user = User.objects.create_superuser(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        client_user = User.objects.get(username=self.username)
        self.assertTrue(client_user.is_staff)
    
    def test_create_author_success(self):
        first_name = "John"
        last_name = "Doe"
        response = self.client.post(reverse('create_author'), {
            "first_name":first_name, 
            "last_name":last_name})
        author_exists = Author.objects.filter(first_name=first_name, last_name=last_name)
        self.assertTrue(author_exists.exists())
        self.assertEqual(response.status_code, 302)
    
    def test_update_author_success(self):
        first_name = 'Old'
        last_name = 'Name'
        old_author = Author.objects.create(first_name=first_name, last_name=last_name)

        updated_data = {
        "first_name": "New",
        "last_name": "Name"
        }
        
        response = self.client.post(reverse('update_author', kwargs={"pk":1}), data=updated_data)
        self.assertEqual(response.status_code, 302)
        new_author = Author.objects.get(pk=1)
        self.assertNotEqual(new_author.first_name, old_author.first_name)
        
    def test_delete_author(self):
        first_name = "John"
        last_name = "Doe"
        author = Author.objects.create(first_name=first_name, last_name=last_name)
        response = self.client.post(reverse('delete_author', kwargs={'pk':1}))
        deleted_author = Author.objects.filter(first_name=first_name)
        self.assertFalse(deleted_author.exists())

       
        

 

       
        

