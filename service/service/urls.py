import sys

from rest_framework.authtoken.views import obtain_auth_token

import library
import todo
from todo.views import ProjectViewSet, ToDoViewSet

sys.path.append('../')

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet, BiographyViewSet, BookViewSet, UserModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('users', UserModelViewSet)
router.register('biographies', BiographyViewSet)
# router.register('articles', ArticleViewSet)
router.register('books', BookViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)
# router.register('base', views.ArticleViewSet, basename='article')
# router.register('model', views.ArticleModelViewSet)
# router.register('custom', views.ArticleCustomViewSet)
filter_router = DefaultRouter()
filter_router.register('custom-django', library.views.ArticleCustomDjangoFilterViewSet)
# router.register('custom-django', views.ArticleCustomDjangoFilterViewSet)
# router.register('custom-django', views.ArticleCustomDjangoFilterViewSet)
# router.register('custom-django', views.ArticleCustomDjangoFilterViewSet)
pagination_router = DefaultRouter()
pagination_router.register('pagenumber', library.views.ArticlePageNumberPaginationViewSet)
pagination_router.register('limitoffset', library.views.ArticleLimitOffsetPaginationViewSet)
pagination_router.register('userpagenumber', library.views.UserPageNumberPaginationViewSet)
pagination_router.register('userlimitoffset', library.views.UserLimitOffsetPaginationViewSet)
pagination_router.register('projectpagenumber', todo.views.ProjectPageNumberPaginationViewSet)
pagination_router.register('projectlimitoffset', todo.views.ProjectLimitOffsetPaginationViewSet)
pagination_router.register('todopagenumber', todo.views.ToDoPageNumberPaginationViewSet)
pagination_router.register('todolimitoffset', todo.views.ToDoLimitOffsetPaginationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    # path('viewsets/', include(router.urls)),
    path('filters/', include(filter_router.urls)),
    path('pagination/', include(pagination_router.urls)),
    path('views/api-view/', library.views.ArticleAPIView.as_view()),
    # path('views/api-view/', userapp.views.UserModelViewSet.as_view)
]
