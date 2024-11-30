from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Power', password='power123')
        self.token = Token.objects.create(user=self.user)
        self.author = Author.objects.create(name="Sally Thorne")
        self.book = Book.objects.create(title="The Hating Game", publication_year=2019, author=self.author)

    def test_create_book(self):
        url = '/api/books/'
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_list(self):
        url = '/api/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


# Create your tests here.
