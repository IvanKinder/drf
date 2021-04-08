import sys

from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
import library
import todo
from todo.views import ProjectViewSet, ToDoViewSet
sys.path.append('../')
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet, BiographyViewSet, BookViewSet, UserModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


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
pagination_router.register('todolimitoffset', todo.views.ToDoLimitOffsetPaginationViewSet)
pagination_router.register('userlimitoffset', library.views.UserLimitOffsetPaginationViewSet)
pagination_router.register('projectpagenumber', todo.views.ProjectPageNumberPaginationViewSet)
pagination_router.register('projectlimitoffset', todo.views.ProjectLimitOffsetPaginationViewSet)
pagination_router.register('todopagenumber', todo.views.ToDoPageNumberPaginationViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='0.1',
        description='Documentation to out project',
        contact=openapi.Contact(email='admin@admin.local'),
        license=openapi.License(name='My_license'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    # path('viewsets/', include(router.urls)),
    path('filters/', include(filter_router.urls)),
    path('pagination/', include(pagination_router.urls)),
    path('views/api-view/', library.views.ArticleAPIView.as_view()),
    # path('views/api-view/', userapp.views.UserModelViewSet.as_view),
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', UserModelViewSet.as_view({'get': 'list'})),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/users/2', include('library.urls', namespace='2')),
]
