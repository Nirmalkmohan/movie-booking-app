from rest_framework import serializers
from .models import Movie, Theater, Showtime, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'

class ShowtimeSerializer(serializers.ModelSerializer):
    seats_available = serializers.IntegerField(read_only=True)
    theater = TheaterSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        many=True
        
