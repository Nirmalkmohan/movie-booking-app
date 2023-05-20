from rest_framework import generics,permissions
from .models import Movie, Theater, Showtime
from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#get all movies listed in the application 
class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# get all theaters listed in application
class TheaterListAPIView(generics.ListAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
# get specific showtime and show movie details along with theater and also available seats
class ShowtimeListAPIView(generics.ListAPIView):
    serializer_class = ShowtimeSerializer

    def get_queryset(self):
        showtime_id = self.request.GET.get('showtime_id')
        queryset = Showtime.objects.all()
        if showtime_id:
            queryset = queryset.filter(id=showtime_id)
        return queryset

#  view handles booking , this view is protected by token authentication
class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': 'Ticket booked successfully'}, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# view allows to search by location  will return the movies in that location with theater details
class MoviesByLocationView(APIView):
    def get(self, request, format=None):
        user_location = request.GET.get('location')
        showtimes = Showtime.objects.filter(theater__location=user_location)
        serializer = ShowtimeSerializer(showtimes, many=True)
        return Response(serializer.data)
    

# view allows to search by movies will return theaters the movie is playing along with showtime and seat availability
class TheaterByMovieView(APIView):
    def get(self, request, format=None):
        user_movie = request.GET.get('movie')  
        showtimes = Showtime.objects.filter(movie__name=user_movie)
        serializer = ShowtimeSerializer(showtimes, many=True)
        return Response(serializer.data)
    
