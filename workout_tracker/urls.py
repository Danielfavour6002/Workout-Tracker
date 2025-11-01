from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/workouts/', include('api.workout.urls')),
    path('api/', include('api.users.urls')),
    path('api/auth/', include('api.auths.urls')),
    path('api/exercises/', include('api.exercise.urls')),
    # path('api/analytics', include('api.analytics.urls')),
    
    # path('api/', include('api.reports.urls')),
]
