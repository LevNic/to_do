from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from todo_app.models import Project, ToDo
from users.serializer import UserModelSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
