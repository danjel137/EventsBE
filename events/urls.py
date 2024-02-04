from django.urls import path
from . import views
from .views import RegisterUser, LoginView

urlpatterns = [
    path('getPhotoList/', views.get_photo_list),
    path('getPhotoById/<int:id>/', views.get_photo_by_id),
    path('addPhoto/', views.add_photo),
    path('deletePhoto/<int:id>/', views.delete_photo),
    path('singUp/', RegisterUser.as_view()),
    path('login/', LoginView.as_view()),
]
