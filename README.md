# movie-booking-app
a movie ticket booking application built-in Django which include - Ability to view all the movies playing in your city Ability to check all cinemas in which a movie is playing along with all the showtimes For each showtime, check the availability of seats User Sign up and login  Ability to book a ticket.

Movie Booking API
This project provides an API for movie booking, including endpoints for retrieving movie details, theater details, showtimes, booking tickets, and searching by location or movie.

Endpoints

User Registration
Endpoint: /user/signup/
Method: POST
Parameters: User data (username, email, password)
Description: This endpoint handles user registration. It expects a JSON payload with the required user data. If the registration is successful, it returns a response with the message "User registered successfully" and the HTTP status code 201 Created. If there are any validation errors, it returns a response with the validation errors and the HTTP status code 400 Bad Request.

User Login
Endpoint: /user/login/
Method: POST
Parameters: User credentials (username, password)
Description: This endpoint handles user login. It expects a JSON payload with the user's credentials. If the credentials are valid, it generates an authentication token using the Token model provided by Django REST Framework. The token is returned in the response JSON along with the message "User logged in successfully".

User Logout
Endpoint: /user/logout/
Method: POST
Parameters: User token (authentication header)
Description: This endpoint handles user logout. It expects an authentication token to be provided in the request's Authorization header using the format "Token <token>". If the token is valid, it is deleted from the database, effectively logging the user out. The endpoint returns a response with the message "User logged out successfully".
  

Movie List
Endpoint: /booking/movies/
Method: GET
Description: This endpoint returns a list of all movies available in the application. It retrieves the movie objects from the database and serializes them using the MovieSerializer.

Theater List
Endpoint: /booking/theaters/
Method: GET
Description: This endpoint returns a list of all theaters available in the application. It retrieves the theater objects from the database and serializes them using the TheaterSerializer.

Showtime List
Endpoint: /booking/showtimes/
Method: GET
Parameters: showtime_id (optional)
Description: This endpoint returns a list of showtimes. If a showtime_id parameter is provided in the request, it filters the showtimes to retrieve a specific showtime by its ID. The showtimes are serialized using the ShowtimeSerializer.

Create Booking
Endpoint: /booking/bookings/
Method: POST
Description: This endpoint handles booking tickets. It requires authentication, and only authenticated users can access it. It expects a JSON payload with the required booking data. If the booking is successful, it returns a response with the message "Ticket booked successfully" and the HTTP status code 201 Created.

Movies by Location
Endpoint: /booking/location/
Method: GET
Parameters: location
Description: This endpoint allows searching for movies by location. It retrieves the showtimes for theaters in the specified location and returns the serialized showtime objects.

Theaters by Movie
Endpoint: /booking/movie/
Method: GET
Parameters: movie
Description: This endpoint allows searching for theaters playing a specific movie. It retrieves the showtimes for the specified movie and returns the serialized showtime objects.

Permissions
The API includes permissions to control access to certain endpoints:

IsAuthenticated: This permission class is used for the BookingCreateAPIView to restrict access to authenticated users only. Only authenticated users can book tickets.

Setup and Usage
To run this project locally, follow these steps:

Install the required dependencies specified in the project's requirements.txt file.
Set up your Django project and database configuration.
Run the Django development server.