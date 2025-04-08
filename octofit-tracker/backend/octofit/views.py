from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response

def api_root(request):
    """
    Root API endpoint providing links to other endpoints.
    """
    base_url = request.build_absolute_uri('/').rstrip('/')
    api_url = f"{base_url}/api/v1"  # Define the API versioning URL
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

# Added suffix method to each viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def suffix(self, request):
        return Response({'suffix': 'users'})

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False, methods=['get'])
    def suffix(self, request):
        return Response({'suffix': 'teams'})

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def suffix(self, request):
        return Response({'suffix': 'activities'})

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def suffix(self, request):
        return Response({'suffix': 'leaderboard'})

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def suffix(self, request):
        return Response({'suffix': 'workouts'})