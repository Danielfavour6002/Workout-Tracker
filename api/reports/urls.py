from django.urls import path
from . import views
urlpatterns = [
    path("<uuid:pk>/summary/", views.WorkoutSummaryAPIView.as_view(), name="workout_summary"),
    path("<uuid:pk>/progress/", views.WorkoutProgressAPIView.as_view(), name="workout_progress"),
    path("<uuid:pk>/report/", views.WorkoutReportAPIView.as_view(), name="workout_report"),
]
