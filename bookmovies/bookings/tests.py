from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Showtime, Movie, Theater
from user_accounts.models import CustomUser
from rest_framework.authtoken.models import Token

class MovieListAPITestCase(APITestCase):
    def test_get_movies(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TheaterListAPITestCase(APITestCase):
    def test_get_theaters(self):
        url = reverse('theater-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ShowtimeListAPITestCase(APITestCase):
    def test_get_showtimes(self):
        url = reverse('showtime-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_showtime_by_id(self):
        Movie.objects.create(name='Test Movie', poster='', description='Test Description')
        Theater.objects.create(name='Test Theater', location='Test Location')
        showtime = Showtime.objects.create(movie_id=1, theater_id=1, start_time='2023-05-20 10:00:00', end_time='2023-05-20 12:00:00', seats_available=100)
        url = reverse('showtime-list')
        response = self.client.get(url, {'showtime_id': showtime.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], showtime.id)


class BookingCreateAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user)
        
        Movie.objects.create(name='Test Movie', poster='', description='Test Description')
        Theater.objects.create(name='Test Theater', location='Test Location')
        self.showtime = Showtime.objects.create(movie_id=1, theater_id=1, start_time='2023-05-20 10:00:00', end_time='2023-05-20 12:00:00', seats_available=100)

    def test_create_booking(self):
        url = reverse('booking-create')
        data = {
            'user': self.user.id,
            'showtime': self.showtime.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MoviesByLocationAPITestCase(APITestCase):
    def test_get_movies_by_location(self):
        url = reverse('movies-by-location')
        response = self.client.get(url, {'location': 'bengaluru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TheatersByMovieAPITestCase(APITestCase):
    def test_get_theaters_by_movie(self):
        url = reverse('theater-by-movie')
        response = self.client.get(url, {'movie': 'Avengers'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
