from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Photo
from .serializers import PhotoSerializer, UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_photo_list(request):
    photos = Photo.objects.all().order_by('-id')
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_photo_by_id(request, id):
    photo = get_object_or_404(Photo, id=id)
    serializer = PhotoSerializer(photo)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_photo(request):
    serializer_new_data = PhotoSerializer(data=request.data)
    if serializer_new_data.is_valid():
        added_item = serializer_new_data.save()
        return Response(data={"message": f"Object with id={added_item.id} added"}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_photo(request, id):
    try:
        photo = get_object_or_404(Photo, id=id)
        photo.delete()
        return Response(data={"message": f"Object {id} deleted"})
    except Exception as e:
        return Response(data={"message": f"Failed to delete photo: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"message": "error"}, status=500)

        serializer.save()
        user = User.objects.get(email=serializer.data["email"])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({"status": 403, "payload": serializer.data, "token": str(token_obj)})


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generating a token for the user
            token_obj, _ = Token.objects.get_or_create(user=user)

            # Include additional fields in the response
            response_data = {
                "status": 403,
                "payload": UserSerializer(user).data,
                "token": str(token_obj),
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(data={"message": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user based on provided username and password
        user = authenticate(username=username, password=password)

        if user:
            # If authentication is successful, generate or retrieve a token
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response({"status": 200, "token": str(token_obj)})
        else:
            # If authentication fails, return an error response
            return Response({"message": "Invalid credentials"}, status=401)
