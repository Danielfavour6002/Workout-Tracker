from django.db import models

# Create your models here.
class Exercise(models.Model):
    class ExerciseCategory(models.TextChoices):
        CARDIO = 'cardio', 'cardio'
        STRENGTH = 'strength', 'strength'
        FLEXIBILITY = 'flexibility', 'flexibility'
    class MuscleGroup(models.TextChoices):
        CHEST = 'chest', 'chest'    
        BACK = 'back', 'back'
        LEGS = 'legs', 'legs'
        ARMS = 'arms', 'arms'
        CORE = 'core', 'core'
        ALL = 'all', 'all'
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=ExerciseCategory.choices, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    muscle_group = models.CharField(max_length=20, choices=MuscleGroup.choices, null=True, blank=True)

    def __str__(self):
        return self.name
    