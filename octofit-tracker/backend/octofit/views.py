from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

def api_root(request):
    """
    Root API endpoint providing links to other endpoints.
    """
    base_url = request.build_absolute_uri('/').rstrip('/')
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "urls": {
            "users": f"{base_url}/users/",
            "teams": f"{base_url}/teams/",
            "activities": f"{base_url}/activities/",
            "leaderboard": f"{base_url}/leaderboard/",
            "workouts": f"{base_url}/workouts/",
        },
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    suffix = 'users'

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    suffix = 'teams'

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    suffix = 'activities'

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    suffix = 'leaderboard'

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    suffix = 'workouts'
