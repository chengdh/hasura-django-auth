from rest_framework.generics import GenericAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .models import Customer,Agent,Contract
from .serializers import CustomerSerializer,AgentSerializer,ContractSerializer

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

class CustomerExportViewSet(XLSXFileMixin, ListAPIView):
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "是", False: "否"}
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '客户信息.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    header = {
        'tab_title': "客户资料",
        'header_title': "客户资料",
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
    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 


class AgentExportViewSet(XLSXFileMixin, ListAPIView):
    """居间资料导出

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "是", False: "否"}
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '居间信息.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 



    header = {
        'tab_title': "居间资料",
        'header_title': "居间资料",
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
class ContractExportViewSet(XLSXFileMixin, ListAPIView):
    """合同导出

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "是", False: "否"}
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '合同资料.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 
    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 


    header = {
        'tab_title': "合同资料",
        'header_title': "合同资料",
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