import sys
sys.path.append('../')
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet, BiographyViewSet, BookViewSet, UserModelViewSet


app_name = 'library'

urlpatterns = [
    path('', UserModelViewSet.as_view({'get': 'list'})),
]
