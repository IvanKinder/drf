from django.test import TestCase
import json

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from library.models import Author, Book
from library.views import AuthorModelViewSet


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'lastname': 'Пушкин', 'birthday_year': 1799}, format='json')
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/', {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.put(f'/api/authors/{author.uuid}/', {'lastname': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')
        client.login(username='admin', password='admin12345')
        response = client.put(f'/api/authors/{author.uuid}/', {'first_name': 'Грин', 'last_name': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(uuid=author.uuid)
        self.assertEqual(author.last_name, 'Грин')
        self.assertEqual(author.birthday_year, 1880)
        client.logout()


class TestBookViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        book = Book.objects.create(name='Пиковая дама', author=author)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')
        self.client.login(username='admin', password='admin12345')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и людмила', 'author': book.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name, 'Руслан и людмила')

    def test_edit_mixer(self):
        book = mixer.blend(Book)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')
        author = Author.objects.create(last_name='Пушкин', birthday_year=1799)
        self.client.login(username='admin', password='admin12345')
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан и людмила', 'author': author.uuid})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.name, 'Руслан и людмила')

# ниже get работает если закомментировать author serializer в book serializer

    def test_get_detail(self):
        book = mixer.blend(Book, name='Алые паруса')
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['name'], 'Алые паруса')

    def test_get_detail_author(self):
        book = mixer.blend(Book, author__first_name='Грин')
        # print(Author.objects.get(uuid=book.author.uuid))
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        author_uuid = response_book['author'][0].split('/')[-2]
        author_first_name = Author.objects.get(uuid=author_uuid).first_name
        self.assertEqual(author_first_name, 'Грин')


