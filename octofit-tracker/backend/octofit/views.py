from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

def api_root(request):
    base_url = "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/api/v1"
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "urls": {
            "users": f"{base_url}/users/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "teams": f"{base_url}/teams/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "activities": f"{base_url}/activities/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "leaderboard": f"{base_url}/leaderboard/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "workouts": f"{base_url}/workouts/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
        },
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
