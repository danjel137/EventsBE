from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from .models import Photo
from .serializers import PhotoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
