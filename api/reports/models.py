from django.db import models
import uuid

from api.workout.models import WorkoutExercises, WorkoutSchedule

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    workout = models.ForeignKey(WorkoutSchedule, on_delete=models.CASCADE, related_name="report" )
    date = models.DateTimeField(auto_now_add=True)
    total_sets = models.PositiveIntegerField(null=True, blank=True)
    total_reps = models.PositiveIntegerField(null=True, blank=True)
    total_weights = models.PositiveIntegerField(null=True, blank=True)
    total_duration = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"report for {self.workout.title} on {self.date.date()}"

class ReportExercise(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="report_exercise")
    workout_exercise = models.ForeignKey(WorkoutExercises, on_delete=models.CASCADE)
    weights_lifted = models.DecimalField(max_digits=5, decimal_places=1)
    reps_completed = models.PositiveIntegerField(default=0)
    sets_completed = models.PositiveIntegerField(default=0)
