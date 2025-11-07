from django.urls import path
from . import views
urlpatterns = [
    path("", views.ListCreateExerciseAPIView.as_view(), name="exercise"),
    path("<uuid:pk>/", views.RetrieveUpdateDeleteExerciseAPIView.as_view(), name="workouts_retrieve"),

]
