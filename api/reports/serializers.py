from rest_framework import serializers
from api.workout.models import WorkoutSchedule
from api.reports.models import Report, ReportExercise
from django.db.models import Sum, Func, F

class WorkoutSummarySerializer(serializers.Serializer):
    workout_name = serializers.CharField(read_only=True)
    total_exercises = serializers.IntegerField()
    total_reps = serializers.IntegerField()
    total_sets = serializers.IntegerField()

class ReportSerializer(serializers.Serializer):
    total_sets = serializers.SerializerMethodField()
    total_reps = serializers.SerializerMethodField()
    total_weights = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ["date", "total_sets", "total_reps", "total_weights", "total_duration"]
    
    def get_total_sets(self,obj):
        return obj.report_exercise.aggregate(total_sets=Sum("sets_completed"))["total_sets"] or 0
    def get_total_reps(self,obj):
        return obj.report_exercise.aggregate(total_reps=Sum("reps_completed"))["total_reps"] or 0
    def get_total_weights(self,obj):
        return obj.report_exercise.aggregate(total_weights=Sum("weights_lifted"))["total_weights"] or 0
    def get_total_duration(self,obj):
       return obj.workout.duration or 0
        

class WorkoutProgressSerializer(serializers.Serializer):
    progress = ReportSerializer()
    trend = serializers.CharField()

class WorkoutReportSerializer(serializers.ModelSerializer):
    total_sets = serializers.SerializerMethodField()
    total_reps = serializers.SerializerMethodField()
    total_weight = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ["id", "date", "total_sets", "total_reps", "total_weight", "total_duration"]

    def get_total_sets(self, obj):
        return obj.report_exercise.aggregate(total=Sum("sets_completed"))["total"] or 0

    def get_total_reps(self, obj):
        return obj.report_exercise.aggregate(total=Sum("reps_completed"))["total"] or 0

    def get_total_weight(self, obj):
        return obj.report_exercise.aggregate(total=Sum("weights_lifted"))["total"] or 0

    def get_total_duration(self, obj):
        return obj.workout.duration or 0


class WorkoutMeSerializer(serializers.Serializer):
    total_workouts_completed = serializers.IntegerField()
    best_exercise = serializers.CharField()

class ReportExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportExercise
        fields = ("id", "report", "workout_exercise", "weights_lifted", "sets_completed", "reps_completed")
        read_only_fields = ["id"]


