"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todo_app.views import ProjectModelViewSet, ToDoModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('todo', ToDoModelViewSet)
router.register('project', ProjectModelViewSet)
# router.register('base', ToDoViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserModelViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
