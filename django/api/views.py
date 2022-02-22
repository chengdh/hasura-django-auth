from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RoleSerializer 
from .models import Role


class RoutersView(RetrieveAPIView):
    """
    获取当前用户前端权限
    """
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.get_default_role

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return Role.objects.none()
