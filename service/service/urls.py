import sys

from todo.views import ProjectViewSet, ToDoViewSet

sys.path.append('../')

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet, BiographyViewSet, ArticleViewSet, BookViewSet
from userapp.views import UserModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('users', UserModelViewSet)
router.register('biographies', BiographyViewSet)
router.register('articles', ArticleViewSet)
router.register('books', BookViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/', include(router.urls)),
    path('', include(router.urls)),
]
