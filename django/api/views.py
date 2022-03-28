from rest_framework.generics import GenericAPIView,CreateAPIView,UpdateAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from django_filters import rest_framework as filters
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .serializers import RoleSerializer,SystemFunctionOperateSerializer,OrganizationSerializer,HasuraUserSerializer 
from .models import Role,HasuraUser
from .filters import RoleFilter


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

class RolesExportViewSet(XLSXFileMixin, ListAPIView):
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "是", False: "否"}
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '角色信息.xlsx' 
    xlsx_ignore_headers = ["id","system_function_operates","routers"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 
    # filterset_class = RoleFilter

    header = {
        'tab_title': "my report",
        'header_title': "this is header title",
    }

    column_header = {
       
        'height': 25,
        'style': {
            'fill': {
                'fill_type': 'solid',
                'start_color': 'FFCCFFCC',
            },
            'alignment': {
                'horizontal': 'center',
                'vertical': 'center',
                'wrapText': True,
                'shrink_to_fit': True,
            },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
            },
            'font': {
                'name': 'Arial',
                'size': 14,
                'bold': True,
                'color': 'FF000000',
            },
        },
    }

    body = {
        'style': {
            'fill': {
                'fill_type': 'solid',
                'start_color': 'FFCCFFCC',
            },
            'alignment': {
                'horizontal': 'center',
                'vertical': 'center',
                'wrapText': True,
                'shrink_to_fit': True,
            },
            'border_side': {
                'border_style': 'thin',
                'color': 'FF000000',
            },
            'font': {
                'name': 'Arial',
                'size': 14,
                'bold': False,
                'color': 'FF000000',
            }
        },
        'height': 40,
    }

class UserView(ModelViewSet):
    queryset = HasuraUser.objects.all()
    serializer_class = HasuraUserSerializer
    permission_classes = (IsAuthenticated,)