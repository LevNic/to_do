from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from todo_app.models import Project, ToDo
from users.serializer import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
