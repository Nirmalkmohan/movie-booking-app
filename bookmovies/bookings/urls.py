from django.urls import path

from .views import *

# the url pattern : http://127.0.0.1:8000/booking/ (urlpatterns below)/

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),

    path('theaters/', TheaterListAPIView.as_view(), name='theater-list'),

    path('showtimes/', ShowtimeListAPIView.as_view(), name='showtime-list'),

    path('bookings/', BookingCreateAPIView.as_view(), name='booking-create'),

    path('location/', MoviesByLocationView.as_view(), name='movies-by-location'),

    path('movie/', TheaterByMovieView.as_view(), name='theater-by-movie'),

]
