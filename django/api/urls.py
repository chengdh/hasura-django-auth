from django.urls import include, path
from .github_login_view import GithubLoginView
urlpatterns = [
    path('github/', GithubLoginView.as_view(), name='github_login')
]
