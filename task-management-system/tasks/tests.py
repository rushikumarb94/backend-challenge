from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task, Label

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        Task.objects.create(title='Task 1', owner=self.user)
        Task.objects.create(title='Task 2', owner=self.user)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        task = Task.objects.create(title='Task 1', owner=self.user)
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_update_task(self):
        task = Task.objects.create(title='Task 1', owner=self.user)
        url = reverse('task-detail', args=[task.id])
        data = {'title': 'Updated Task', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task')
        self.assertTrue(Task.objects.get().completed)

    def test_delete_task(self):
        task = Task.objects.create(title='Task 1', owner=self.user)
        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class LabelTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_label(self):
        url = reverse('label-list')
        data = {'name': 'Test Label'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Label.objects.count(), 1)
        self.assertEqual(Label.objects.get().name, 'Test Label')

    def test_list_labels(self):
        Label.objects.create(name='Label 1', owner=self.user)
        Label.objects.create(name='Label 2', owner=self.user)
        url = reverse('label-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_label(self):
        label = Label.objects.create(name='Label 1', owner=self.user)
        url = reverse('label-detail', args=[label.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Label 1')

    def test_update_label(self):
        label = Label.objects.create(name='Label 1', owner=self.user)
        url = reverse('label-detail', args=[label.id])
        data = {'name': 'Updated Label'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Label.objects.get().name, 'Updated Label')

    def test_delete_label(self):
        label = Label.objects.create(name='Label 1', owner=self.user)
        url = reverse('label-detail', args=[label.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Label.objects.count(), 0)