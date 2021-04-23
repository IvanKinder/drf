from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Author, Biography, Article, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.Serializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(serializers.ModelSerializer):
    # authors = serializers.StringRelatedField(many=True)
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializerBase(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)


class UserModelSerializerVersion2(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser',)


