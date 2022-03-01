from django.urls import path
from .github_login_view import GithubLoginView
from .views import RoutersView,PermissionsView,AllPermissionsView
urlpatterns = [
    # path('github/', GithubLoginView.as_view(), name='github_login'),
    path('getAsyncRoutes/', RoutersView.as_view(), name='get_async_routes'),
    path('get_permissions/', PermissionsView.as_view(), name='get_permissions'),
    path('get_all_permissions/', AllPermissionsView.as_view(), name='get_all_permissions'),
]