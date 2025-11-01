from rest_framework import generics, permissions
from api.exercise.models import Exercise
from . import serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ListCreateExerciseAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer

    def get_permissions(self):
        self.permission_classes = [permissions.AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

class RetrieveUpdateDeleteExerciseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()