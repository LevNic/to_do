# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import ToDo, Project
from .serializer import ProjectModelSerializer, ToDoModelSerializer, ProjectModelSerializerBase


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name', 'users']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectModelSerializer
        return ProjectModelSerializerBase


class ToDoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
