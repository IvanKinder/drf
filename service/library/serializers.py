from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Author, Biography, Article, Book


class AuthorSerializer(HyperlinkedModelSerializer):

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


class BookSerializer(HyperlinkedModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class UserModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)


