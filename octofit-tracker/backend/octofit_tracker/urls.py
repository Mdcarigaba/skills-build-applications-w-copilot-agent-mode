from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api_root, UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('api/v1/', api_root, name='api-root'),
    path('', api_root),
    path('', include(router.urls)),
]