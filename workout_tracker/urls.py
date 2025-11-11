from django.contrib import admin
from django.urls import path, include
from api.reports import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/workouts/', include('api.workout.urls')),
    path('api/', include('api.users.urls')),
    path('api/auth/', include('api.auths.urls')),
    path('api/exercises/', include('api.exercise.urls')),
    # path('/', include('api.reports.urls')),
    path("api/workouts/", include("api.reports.urls")),
    path("api/me/progress/", views.UserWorkoutProgress.as_view(), name="user_progress"),
    path("reports/<uuid:report_id>/exercises/", views.ReportExerciseListCreateAPIView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path('api/', include('api.reports.urls')),
]
