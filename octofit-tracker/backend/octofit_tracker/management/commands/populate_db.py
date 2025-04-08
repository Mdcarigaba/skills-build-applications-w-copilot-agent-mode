from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId
from pymongo import MongoClient
from django.conf import settings

print('populate_db command is being loaded')

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Use raw MongoDB commands to clear collections
        client = MongoClient(host=settings.DATABASES['default']['HOST'], port=settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        for user in users:
            user.save()  # Save each user individually to ensure primary key assignment

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-08'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-06'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-05'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=100),
            Leaderboard(team=team2, points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
