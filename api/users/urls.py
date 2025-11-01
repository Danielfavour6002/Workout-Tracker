from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name="create_user"),
    path('users/<int:pk>/profile/', views.UserProfileRetrieveAPIView.as_view(), name="user_profile"),
    path('me/', views.MeAPIView.as_view(), name="me")   
]