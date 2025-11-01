from rest_framework import generics, permissions
from api.workout.models import WorkoutSchedule, WorkoutExercises
from . import serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ListCreateWorkoutAPIView(generics.ListCreateAPIView):
    """create a workout and list all current user workouts"""
    serializer_class = serializers.WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutSchedule.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDeleteWorkoutAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutSchedule.objects.filter(user=self.request.user)

class ListWorkoutExercisesAPIView(generics.ListAPIView):
    serializer_class = serializers.WorkoutExerciseSerializer
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        return WorkoutExercises.objects.filter(workout__id=self.kwargs["pk"], workout__user=self.request.user)

   

        
