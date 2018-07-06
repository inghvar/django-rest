import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestOrdersList(APITestCase):
    @pytest.mark.django_db
    def test_can_get_orders_list(self):
        url = reverse('orders-all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestOrderGet(APITestCase):
    @pytest.mark.django_db
    def test_get(self):
        url = reverse('order', kwargs={'pk': 3})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestOrderDelete(APITestCase):
    @pytest.mark.django_db
    def test_delete(self):
        url = reverse('order', kwargs={'pk': 4})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

