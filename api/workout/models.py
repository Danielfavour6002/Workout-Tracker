from django.db import models
import uuid
from api.users.models import User
# Create your models here.
class WorkoutSchedule(models.Model):
    class WorkoutStatus(models.TextChoices):
        PENDING = 'pending', 'pending'
        COMPLETED = 'completed', 'completed'
        ACTIVE = 'active', 'active'
    class WorkoutFrequency(models.TextChoices):
        DAILY = 'daily', 'daily'
        WEEKLY = 'weekly', 'weekly'
        MONTHLY = 'monthly', 'monthly'
        YEARLY = 'yearly', 'yearly'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_schedules')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=True)
    repeat_frequency = models.CharField(max_length=20, choices=WorkoutFrequency.choices, default=WorkoutFrequency.DAILY)
    repeat_interval = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=WorkoutStatus.choices, default=WorkoutStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"workout {self.title} by {self.user.username}"

class WorkoutExercises(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    workout = models.ForeignKey(WorkoutSchedule, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercises')
    reps = models.PositiveIntegerField(default=1)
    sets = models.PositiveIntegerField(default=1)
    weights = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"{self.workout.title} x {self.exercise.name}"

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # user_id = 
    workout_id = models.ForeignKey(WorkoutSchedule, on_delete=models.CASCADE, related_name="report" )
    report_date = models.DateTimeField(auto_now_add=True)
    weights_lifted = models.DecimalField(max_digits=5, decimal_places=1)
    reps_completed = models.PositiveIntegerField(default=0)
    sets_completed = models.PositiveIntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"report for {self.workout_id.title} on {self.report_date.date}"
