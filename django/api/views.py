from rest_framework.generics import GenericAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RoleSerializer,SystemFunctionOperateSerializer 
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

class PermissionsView(ListAPIView):
    """
    获取当前用户前端权限
    """
    serializer_class = SystemFunctionOperateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        得到角色权限
        """
        return self.request.user.get_default_role.system_function_operates.all()