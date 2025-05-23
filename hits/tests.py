from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artist, Hit


class HitTests(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(first_name="Jan", last_name="Kowalski")
        self.hit = Hit.objects.create(title="Test Song", artist=self.artist)

    def test_get_hits(self):
        url = reverse("hit-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_hit(self):
        url = reverse("hit-list-create")
        hit_data = {"title": "New Song", "artist": self.artist.id}
        response = self.client.post(url, hit_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_hit_detail(self):
        url = reverse("hit-detail", args=[self.hit.title_url])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_hit(self):
        url = reverse("hit-detail", args=[self.hit.title_url])
        hit_data = {"title": "Updated Song", "artist": self.artist.id}
        response = self.client.put(url, hit_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_hit(self):
        url = reverse("hit-detail", args=[self.hit.title_url])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
