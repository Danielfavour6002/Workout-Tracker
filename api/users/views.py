from .serializers import UserSerializer, ProfileSerializer, UserUpdateSerializer
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import User, Profile

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
    '''get a specific user profile (admin only)'''
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        user_id = self.kwargs["pk"]
        return get_object_or_404(Profile, user__id=user_id)

class MeAPIView(generics.RetrieveUpdateAPIView):
    ''' get logged in user's profile and update users profile'''
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

