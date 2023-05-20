from django.contrib import admin
from .models import Movie, Theater, Showtime, Booking

# we have registerd the models here so that we can access the model from django admin interface to create edit and manage data
# pass is added as no other cuzomisation needed now  if any additional customization needed can be modified 

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    pass

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
