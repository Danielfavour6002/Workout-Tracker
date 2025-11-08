from django.shortcuts import get_object_or_404
from rest_framework import serializers
from api.workout.models import WorkoutSchedule, WorkoutExercises
from api.exercise.serializers import ExerciseSerializer

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutSchedule
        exclude = ["user"]
        read_only_fields = ("id", )
       
class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    class Meta:
        model = WorkoutExercises
        fields = ["id", "workout", "exercise", "reps", "sets", "weights"]
        read_only_fields = ["id"]
        
    def perform_create(self, serializer):
        workout = get_object_or_404(
            WorkoutSchedule,
            id=self.kwargs["pk"],
            user=self.request.user
        )
        serializer.save(workout=workout)
