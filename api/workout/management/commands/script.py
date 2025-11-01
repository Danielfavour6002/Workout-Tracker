from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from workout.models import Exercise


class Command(BaseCommand):
    help = "Seeds the database with sample exercises."

    def handle(self, *args, **kwargs):
        exercises = [
            Exercise(name="Bicep Curls", category='strength', description=lorem_ipsum.paragraph(), muscle_group='arms'),
            Exercise(name="Tricep Dips", category='strength', description=lorem_ipsum.paragraph(), muscle_group='arms'),
            Exercise(name="Push Ups", category='strength', description=lorem_ipsum.paragraph(), muscle_group='chest'),
            Exercise(name="Bench Press", category='strength', description=lorem_ipsum.paragraph(), muscle_group='chest'),
            Exercise(name="Squats", category='strength', description=lorem_ipsum.paragraph(), muscle_group='legs'),
            Exercise(name="Lunges", category='strength', description=lorem_ipsum.paragraph(), muscle_group='legs'),
            Exercise(name="Deadlifts", category='strength', description=lorem_ipsum.paragraph(), muscle_group='back'),
            Exercise(name="Pull Ups", category='strength', description=lorem_ipsum.paragraph(), muscle_group='back'),
            Exercise(name="Plank", category='flexibility', description=lorem_ipsum.paragraph(), muscle_group='core'),
            Exercise(name="Crunches", category='strength', description=lorem_ipsum.paragraph(), muscle_group='core'),
            Exercise(name="Running", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='all'),
            Exercise(name="Cycling", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='legs'),
            Exercise(name="Jump Rope", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='all'),
            Exercise(name="Mountain Climbers", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='core'),
            Exercise(name="Burpees", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='all'),
            Exercise(name="Shoulder Press", category='strength', description=lorem_ipsum.paragraph(), muscle_group='arms'),
            Exercise(name="Leg Press", category='strength', description=lorem_ipsum.paragraph(), muscle_group='legs'),
            Exercise(name="Lat Pulldown", category='strength', description=lorem_ipsum.paragraph(), muscle_group='back'),
            Exercise(name="Yoga Stretch", category='flexibility', description=lorem_ipsum.paragraph(), muscle_group='all'),
            Exercise(name="Pilates Roll-Up", category='flexibility', description=lorem_ipsum.paragraph(), muscle_group='core'),
            Exercise(name="Treadmill Walk", category='cardio', description=lorem_ipsum.paragraph(), muscle_group='legs'),
        ]

        Exercise.objects.bulk_create(exercises, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("✅ 20+ exercises seeded successfully!"))
