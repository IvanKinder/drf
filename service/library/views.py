from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import logging
from .filters import ArticleFilter
from .models import Author, Biography, Article, Book
from .serializers import AuthorSerializer, BiographySerializer, ArticleSerializer, BookSerializer, UserModelSerializer, \
    BookSerializerBase, UserModelSerializerVersion2

log = logging.getLogger('service_log')


class AuthorModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


# class ArticleViewSet(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArticleAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        log.info(f'{request.data}; {request.POST}')
        return Response(serializer.data)


# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def article_view(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)


class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer = ArticleSerializer


class ArticleListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer = ArticleSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer = ArticleSerializer


class ArticleDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer = ArticleSerializer


class ArticleCustomDjangoFilterViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter


class ArticlePageNumberPaginationViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleLimitOffsetPagination


class ArticleParamFilterViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        log.info(f'{self.request.data}; {self.request.POST}')
        return articles


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookSerializerBase


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2':
            print('version = 2')
            return UserModelSerializerVersion2
        return UserModelSerializer


class UserPageNumberPaginationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class UserLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination


class UserParamFilterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', '')
        users = User.objects.all()
        if username:
            users = users.filter(name__contains=username)
        log.info(f'{self.request.data}; {self.request.POST}')
        return users
