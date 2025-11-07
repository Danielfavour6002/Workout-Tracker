from django.urls import path
from . import views
urlpatterns = [
    path("", views.ListCreateWorkoutAPIView.as_view(), name="workouts"),
    path("<uuid:pk>/", views.RetrieveUpdateDeleteWorkoutAPIView.as_view(), name="workouts_retrieve"),
    path("<uuid:pk>/exercises/", views.ListCreateWorkoutExercisesAPIView.as_view(), name="workout_exercises")
]
