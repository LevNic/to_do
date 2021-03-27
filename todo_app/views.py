# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import ToDo, Project
from .serializer import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name', 'users']


class ToDoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


# class ToDoViewSet(ViewSet):
#
#     def list(self, request):
#         to_do = ToDo.objects.all()
#         serializer = ToDoModelSerializer(to_do, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         to_do = get_object_or_404(ToDo, pk=pk)
#         serializer = ToDoModelSerializer(to_do)
#         return Response(serializer.data)
