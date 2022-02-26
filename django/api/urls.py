from django.urls import path
from .github_login_view import GithubLoginView
from .views import RoutersView,PermissionsView
urlpatterns = [
    # path('github/', GithubLoginView.as_view(), name='github_login'),
    path('getAsyncRoutes/', RoutersView.as_view(), name='get_async_routes'),
    path('getPermissions/', PermissionsView.as_view(), name='get_permissions'),
]