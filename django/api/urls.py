from django.urls import include, path
from .github_login_view import GithubLoginView
from .views import RoutersView
urlpatterns = [
    path('github/', GithubLoginView.as_view(), name='github_login'),
    path('getAsyncRoutes/', RoutersView.as_view(), name='get_async_routes'),
]
