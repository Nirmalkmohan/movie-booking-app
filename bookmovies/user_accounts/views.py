from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# view handles creating a new user if not success will return a http:400 bad request  response
class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view handles login function has used token based authetication from restframework
class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# view for logout,get user token and deletes the token to log the user out
from rest_framework.exceptions import AuthenticationFailed

class LogoutAPIView(APIView):
    def post(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header and auth_header.startswith('Token '):
            token = auth_header.split(' ')[1]
            Token.objects.filter(key=token).delete()
            return Response({'detail': 'User logged out successfully'})

        raise AuthenticationFailed('Invalid authorization header')

