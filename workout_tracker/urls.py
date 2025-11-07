from django.contrib import admin
from django.urls import path, include
from api.reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/workouts/', include('api.workout.urls')),
    path('api/', include('api.users.urls')),
    path('api/auth/', include('api.auths.urls')),
    path('api/exercises/', include('api.exercise.urls')),
    # path('/', include('api.reports.urls')),
    path("api/workouts/", include("api.reports.urls")),
    path("api/me/progress/", views.UserWorkoutProgress.as_view(), name="user_progress"),
    path("api/me/report_exercise/", views.ReportExerciseView.as_view(), name="report_exercise"),
    # path('api/', include('api.reports.urls')),
]
