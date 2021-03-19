from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from todo.models import Project, ToDo
from library.serializers import UserModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'

