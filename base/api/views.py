from django.http import JsonResponse
from rest_framework.response import Response
# Going to use function based views not class
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # encrypy into the token
        token['username'] = user.username
        # ...

        return token

# class
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# add decorater ~ GET for now
# create a view
@api_view(['GET'])
def getRoutes(request):
    # routes
    routes = [
        # endpoint for token
        # submit username and password ~ will receive access and refresh token
        '/api/token',
        
        # will give you a refreshed token from the backend
        '/api/token/refresh',
    ]
    # serialize information for False
    return Response(routes)