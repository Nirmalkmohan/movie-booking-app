from user_accounts.models import CustomUser
from django.db import models

# for adding a movie to the database
class Movie(models.Model):
    name = models.CharField(max_length=100)
    poster=models.ImageField(upload_to='movies',blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# for adding theaters to database
class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# for adding showtimes this model has foreignkey relations with Movies and Theater models 
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    seats_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.movie.name} at {self.theater.name}"


# this model stores booking details have relationship with customuser model for user identification and showtime model for identifying booking details
class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
 
    def __str__(self):
        return f"Booking #{self.pk} - {self.user.username} - {self.showtime.movie.name} at {self.showtime.theater.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.showtime.seats_available -= 1
        self.showtime.save()

