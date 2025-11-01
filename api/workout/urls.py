from django.urls import path
from . import views
urlpatterns = [
    path("/", views.ListCreateWorkoutAPIView.as_view(), name="workouts"),
    path("<int:pk>/", views.RetrieveUpdateDeleteWorkoutAPIView(), name="workouts_retrieve"),
    path("/<int:pk>/exercises/", views.ListWorkoutExercisesAPIView.as_view(), name="workouts")
]
