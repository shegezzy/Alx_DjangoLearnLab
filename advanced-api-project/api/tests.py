from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookApiTests(APITestCase):
    def setUp(self):
        # Creates a test author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Creates a test book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        
        # Creates a test user
        self.user = User.objects.create_user(username="Dear", password="password123")
        
        # Authenticated client
        self.authenticated_client = self.client
        self.authenticated_client.login(username="Power", password="power123")
        
    def test_create_book(self):
        url = '/books/'
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id,
        }
        
        # Ensure the book is created
        response = self.authenticated_client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, "Harry Potter and the Chamber of Secrets")

    def test_get_books(self):
        url = '/books/'
        response = self.client.get(url)  # Unauthenticated user
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book created in setup
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_get_book_detail(self):
        url = f'/books/{self.book.id}/'
        response = self.client.get(url)  # Unauthenticated user
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter and the Philosopher's Stone")

    def test_update_book(self):
        url = f'/books/{self.book.id}/update/'
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.id,
        }
        
        response = self.authenticated_client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh the book instance from the database
        self.assertEqual(self.book.title, "Harry Potter and the Prisoner of Azkaban")
        self.assertEqual(self.book.publication_year, 1999)

    def test_delete_book(self):
        url = f'/books/{self.book.id}/delete/'
        
        # Ensure the book is deleted
        response = self.authenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        url = '/books/?title=Harry Potter'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_filter_books_by_author(self):
        url = f'/books/?author__name={self.author.name}'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], self.author.name)

    def test_search_books_by_title(self):
        url = '/books/?search=Harry Potter'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        url = '/books/?search=Rowling'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        url = '/books/?ordering=publication_year'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_permissions_for_create_update_delete(self):
        # Unauthenticated user should not be able to create, update, or delete a book
        url = '/books/'
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id,
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        url = f'/books/{self.book.id}/update/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        url = f'/books/{self.book.id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



# Create your tests here.
