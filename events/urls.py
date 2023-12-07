from django.urls import path
from . import views

urlpatterns = [
    path('getPhotoList/', views.getPhotoList),
    path('getPhotoById/<int:id>/', views.getPhotoById),
    path('addPhoto/', views.addPhoto),
    path('deletePhoto/<int:id>/', views.deletePhoto),
]
