from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Photo
from .serializers import PhotoSerializer,  UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PhotoAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def getPhotoList(request):
        photos = Photo.objects.all().order_by('-id')
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getPhotoById(request, id):
        photos = Photo.objects.get(id=id)
        serializer = PhotoSerializer(photos, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def addPhoto(request):
        serializerNewData = PhotoSerializer(data=request.data)
        if serializerNewData.is_valid():
            added_item = serializerNewData.save()
            return Response(data={"message": f"Object with id={added_item.id} added"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"message": f"Object did not found"})

    @api_view(['DELETE'])
    def deletePhoto(request, id):
        try:
            photo = get_object_or_404(Photo, id=id)
            photo.delete()
            return Response(data={"message": f"Object {id} deleted"})
        except Photo.DoesNotExist:
            return Response(data={"message": "Photo does not exist"}, status=404)
        except Exception as e:
            return Response(data={"message": f"Failed to delete photo: {str(e)}"}, status=500)


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"message": "error"}, status=500)
        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({"status": 403, "payload": serializer.data, "token": str(token_obj)})


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
