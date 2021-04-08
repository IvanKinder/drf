from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from library.views import log
from todo.models import Project, ToDo
from todo.serializers import ProjectSerializer, ToDoSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoPageNumberPaginationViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination


class ProjectPageNumberPaginationViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ToDoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


