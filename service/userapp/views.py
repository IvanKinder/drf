from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from library.views import log
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


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
