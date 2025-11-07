from rest_framework.views import APIView
from api.reports.serializers import WorkoutSummarySerializer, WorkoutProgressSerializer, WorkoutReportSerializer, WorkoutMeSerializer, ReportExerciseSerializer
from django.db.models import Sum, Count
from rest_framework.response import Response
from api.workout.models import WorkoutSchedule, WorkoutExercises
from api.reports.models import Report, ReportExercise
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
class WorkoutSummaryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        workout = get_object_or_404(WorkoutSchedule, pk=pk, user=request.user)
        exercises = WorkoutExercises.objects.filter(workout=workout)
        serializer = WorkoutSummarySerializer(
            {"workout_name" : workout.title,
             "total_exercises" : exercises.aggregate(total_exercises=Count("exercise"))["total_exercises"],
             "total_reps" : exercises.aggregate(total_reps=Sum("reps"))["total_reps"],
             "total_sets" : exercises.aggregate(total_sets=Sum("sets"))["total_sets"],
             } )
        return Response(serializer.data)
    
class WorkoutProgressAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        # 1. Ensure workout belongs to the user
        workout = get_object_or_404(WorkoutSchedule, id=pk, user=request.user)

        # 2. Get all past workout reports sorted oldest → newest
        reports = Report.objects.filter(workout=workout).order_by("date")

        # 3. Cannot compare if only one report exists
        if reports.count() < 2:
            return Response({"detail": "Not enough workout sessions to show progress."}, status=200)

        # 4. First session vs most recent session
        first = reports.first()
        last = reports.last()

        # 5. Calculate percentage changes safely
        def percent_change(old, new):
            if old == 0:
                return None
            return round(((new - old) / old) * 100, 2)

        sets_change = percent_change(first.total_sets, last.total_sets)
        reps_change = percent_change(first.total_reps, last.total_reps)
        weight_change = percent_change(first.total_weight, last.total_weight)

        # 6. Evaluate progress trend
        if weight_change is None:
            trend = "not enough data"
        elif weight_change > 15:
            trend = "improving"
        elif weight_change < -10:
            trend = "declining"
            trend
        else:
            trend = "stable"

        # 7. Response Data Returned to Frontend
        return Response({
            "workout": workout.title,
            "sessions_count": reports.count(),
            "trend": trend,
            "progress": {
                "sets_change_percent": sets_change,
                "reps_change_percent": reps_change,
                "weight_change_percent": weight_change
            }
        }, status=200)

class WorkoutReportAPIView(APIView):
    def get(self, request, pk):
        # Ensure workout belongs to user
        workout = get_object_or_404(WorkoutSchedule, id=pk, user=request.user)

        # Try to get the latest report session
        report = Report.objects.filter(workout=workout).order_by("-date").first()

        # If no report exists → generate one
        if not report:
            exercises = WorkoutExercises.objects.filter(workout=workout)

            total_sets = exercises.aggregate(total=Sum("sets"))["total"] or 0
            total_reps = exercises.aggregate(total=Sum("reps"))["total"] or 0
            total_weights = exercises.aggregate(total=Sum("weights"))["total"] or 0

            report = Report.objects.create(
                workout=workout,
                total_sets=total_sets,
                total_reps=total_reps,
                total_weights=total_weights,
                total_duration=workout.duration,
                notes="Auto-generated session report."
            )

        # Prepare structured response data
        summary = {
            "workout_name": workout.title,
            "total_exercises": workout.workout_exercises.count(),
            "total_reps": report.total_reps,
            "total_sets": report.total_sets,
            "total_duration": report.total_duration,
        }

        progress = {
            "progress": report,
            "trend": "stable"  # Hard-coded for now (could compute later)
        }

        data = {
            "report_id": report.id,
            "workout": workout.title,
            "summary": summary,
            "progress": progress,
            "insights": "Keep going! You're doing great."
        }

        serializer = WorkoutReportSerializer(data)
        return Response(serializer.data)

        
class UserWorkoutProgress(APIView):
    def get(self, request):
        serializer = WorkoutMeSerializer({
            "total_workouts_completed" : WorkoutSchedule.objects.filter(user=request.user).count(),
            "best_exercise" : ReportExercise.objects.select_related('workout_exercises').values('workout_exercise__exercise__name').annotate(count=Count('workout_exercise')).order_by('-count').first()['workout_exercise__exercise__name']
        })
        return Response(serializer.data)

class ReportExerciseView(generics.ListCreateAPIView):
    
    serializer_class = ReportExerciseSerializer
    def get_queryset(self):
        return ReportExercise.objects.filter(report__workout__user=self.request.user)
    