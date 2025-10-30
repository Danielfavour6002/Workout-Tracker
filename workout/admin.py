from django.contrib import admin
from . import models
from users.models import User, Profile
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(models.Exercise)
admin.site.register(models.WorkoutSchedule)
admin.site.register(models.WorkoutExercises)
admin.site.register(models.Report)
