from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import list_route

from .models import Task, Project, Habbit, Dailies, DailiesDoneList
from .serializers import TaskSerializers, ProjectSerializers, HabbitSerializers, DailiesSerializers

from pprint import pprint
import json
from django.core import serializers
from django.forms.models import model_to_dict

from django.core.serializers.json import DjangoJSONEncoder

class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializers

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['GET'])
    def get_task_project(self, request, pk=None):
        if pk is None:
            return Response({"message": "Wrong project id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task_list = Task.objects.filter(project=pk)
            serializer = TaskSerializers(task_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "can not find user project"}, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializers

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabbitViewSet(viewsets.ModelViewSet):

    serializer_class = HabbitSerializers

    def get_queryset(self):
        return Habbit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DailiesViewSet(viewsets.ModelViewSet):

    serializer_class = DailiesSerializers

    def get_queryset(self):
        return Dailies.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @list_route(methods=['GET'])
    def get_dailies_with_done(self, request):
        user_dailies = Dailies.objects.filter(user=self.request.user)
        out = []

        for dailie in user_dailies:
            dailies_done = DailiesDoneList.objects.filter(dailies=dailie.id)
            dailie_with_done_list = dailie.__dict__

            dailies_done_list = [model_to_dict(elem) for elem in dailies_done]

            dailie_with_done_list['done_list'] = dailies_done_list
            del dailie_with_done_list['_state']

            out.append(dailie_with_done_list)

        data = json.dumps(out, indent=1, cls=DjangoJSONEncoder)
        return Response(data, status=status.HTTP_200_OK)
