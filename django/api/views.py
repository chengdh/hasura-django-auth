from rest_framework.generics import GenericAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoleSerializer,SystemFunctionOperateSerializer,OrganizationSerializer,HasuraUserSerializer 
from .models import Role,HasuraUser


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

class AllPermissionsView(RetrieveAPIView):
    """
    获取当前用户前端权限,包括roles/orgs/permissions
    """
    serializer_class = HasuraUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return HasuraUser.objects.none()