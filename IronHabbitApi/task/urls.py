from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from .views import TaskViewSet, ProjectViewSet, HabbitViewSet, DailiesViewSet

router = routers.DefaultRouter()
router.register('task', TaskViewSet, basename="Task")
router.register('project', ProjectViewSet, basename='Project')
router.register('habbit', HabbitViewSet, basename='Habbit')
router.register('dailies', DailiesViewSet, basename='Dailies')

urlpatterns = [
    path('', include(router.urls)),
]
