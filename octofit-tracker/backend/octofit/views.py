from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

def api_root(request):
    base_url = "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev"
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "urls": {
            "users": "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/users/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "teams": "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/teams/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "activities": "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/activities/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "leaderboard": "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/leaderboard/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
            "workouts": "https://organic-space-sniffle-vwwxpq65pqx2pwp6-8000.app.github.dev/workouts/", # CODESPACE NAME: organic-space-sniffle-vwwxpq65pqx2pwp6
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
