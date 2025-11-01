from rest_framework import serializers
from api.workout.models import WorkoutSchedule, WorkoutExercises
from api.exercise.serializers import ExerciseSerializer

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutSchedule
        fields = "__all__"
        exclude = ["user"]
        read_only_fields = ["id"]



class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = WorkoutExercises
        fields = ["id", "workout", "exercise", "reps", "sets", "weights"]
        read_only_fields = ["id"]

