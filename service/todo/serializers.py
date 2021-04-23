from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from todo.models import Project, ToDo


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        # fields = ('project', 'text', 'created_at', 'updated_at',  'is_active', 'user',)
        fields = '__all__'
