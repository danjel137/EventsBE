from django.urls import path
from . import views
from .views import RegisterUser, PhotoAPI, LoginView

urlpatterns = [
    path('getPhotoList/', PhotoAPI.getPhotoList),
    path('getPhotoById/<int:id>/', PhotoAPI.getPhotoById),
    path('addPhoto/', PhotoAPI.addPhoto),
    path('deletePhoto/<int:id>/', PhotoAPI.deletePhoto),
    path('singUp/', RegisterUser.as_view()),
    path('login/', LoginView.as_view()),
]
