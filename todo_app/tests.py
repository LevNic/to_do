import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from users.views import UserModelViewSet
from .models import Project
from users.models import User


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/user/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/user/',
                               {'uuid': '2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', 'username': 'Пушкин',
                                'first_name': 'Саша', 'last_name': 'Пуш', 'age': 99, 'mail': 'mail@mail.ru'},
                               format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        user = User.objects.create(uuid='2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', username='Пушкин',
                                   first_name='Саша', last_name='Пуш', age=99, mail='mail@mail.ru')
        client = APIClient()
        response = client.get(f'/api/user/{user.uuid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(uuid='2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', username='Пушкин',
                                   first_name='Саша', last_name='Пуш', age=99, mail='mail@mail.ru')
        client = APIClient()
        response = client.put(f'/api/user/{user.id}/', {'username': 'Грин', 'age': 80})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(uuid='2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', username='Пушкин',
                                   first_name='Саша', last_name='Пуш', age=99, mail='mail@mail.ru')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/authors/{user.id}/', {'name': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.name, 'Грин')
        self.assertEqual(user.age, 80)
        client.logout()

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/user/',
                               {'uuid': '2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', 'username': 'Пушкин',
                                'first_name': 'Саша', 'last_name': 'Пуш', 'age': 99, 'mail': 'mail@mail.ru'},
                               format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProjectViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User.objects.create(uuid='2e9cc887-8d7a-4afd-bf9d-d05cea5e1241', username='Пушкин',
                                   first_name='Саша', last_name='Пуш', age=99, mail='mail@mail.ru')
        project = Project.objects.create(uuid='87e8f197-00ca-480f-a6e3-411a72edfe4e', name='Пиковая дама',
                                         link='/pycharm/django_test_manage.py', users=user)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/project/{project.uuid}/', {'name': 'Руслан и Людмила',
                                                                     'users': project.users.uuid})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(uuid=project.uuid)
        self.assertEqual(project.name, 'Руслан и Людмила')

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/books/{project.uuid}/', {'name': 'Руслан и Людмила', 'users': project.users.uuid})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Project.objects.get(uuid=project.uuid)
        self.assertEqual(book.name, 'Руслан и Людмила')


