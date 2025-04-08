from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

def api_root(request):
    base_url = request.build_absolute_uri('/').rstrip('/')
    api_url = f"{base_url}/api/v1"
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "urls": {
            "users": f"{api_url}/users/",
            "teams": f"{api_url}/teams/",
            "activities": f"{api_url}/activities/",
            "leaderboard": f"{api_url}/leaderboard/",
            "workouts": f"{api_url}/workouts/",
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
