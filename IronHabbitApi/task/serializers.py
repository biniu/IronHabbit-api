from rest_framework import serializers
from .models import Task, Project, Habbit


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class HabbitSerializers(TaskSerializers):
    class Meta:
        model = Habbit
        fields = '__all__'
