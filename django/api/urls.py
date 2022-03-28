from django.urls import path,include
from .github_login_view import GithubLoginView
from .views import RoutersView,PermissionsView,AllPermissionsView,RolesExportViewSet,UserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user_maintain', UserView)
urlpatterns = [
    # path('github/', GithubLoginView.as_view(), name='github_login'),
    path('getAsyncRoutes/', RoutersView.as_view(), name='get_async_routes'),
    path('get_permissions/', PermissionsView.as_view(), name='get_permissions'),
    path('get_all_permissions/', AllPermissionsView.as_view(), name='get_all_permissions'),
    path('export_api_role/', RolesExportViewSet.as_view(), name='export_api_role'),
    path('', include(router.urls)),
]