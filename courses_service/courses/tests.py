from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CourseListAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('course-list')

    def test_get_courses_list_unauthenticated(self):
        """
        Test that unauthenticated users cannot access the courses list endpoint.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_courses_list_authenticated(self):
        """
        Test that authenticated users can access the courses list endpoint.
        """
        token = 'testcoursetoken'
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_courses_list_paginated(self):
        """
        Test that the courses list can be paginated.
        """
        token = 'testcoursetoken'
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get(f'{self.url}?page=1&page_size=5')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
