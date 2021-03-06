from rest_framework.generics import GenericAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .models import Customer,Agent,Contract,MthAdjust,MthAdjustLine,MthDraftCustomerBillLine,MthDraftCustomerBill,MthCustomerBill,MthAgentBill
from .serializers import CustomerSerializer,AgentSerializer,ContractSerializer,MthAdjustLineSerializer,MthDraftCustomerBillLineSerializer,MthCustomerBillLineSerializer,MthAgentBillLineSerializer

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
    xlsx_boolean_labels = {True: "???", False: "???"}
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    header = {
        'tab_title': "????????????",
        'header_title': "????????????",
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
    """??????????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 



    header = {
        'tab_title': "????????????",
        'header_title': "????????????",
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
    """????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    renderer_classes = (XLSXRenderer,)
    filename = '????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 
    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 


    header = {
        'tab_title': "????????????",
        'header_title': "????????????",
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

class MthAdjustExportViewSet(XLSXFileMixin, ListAPIView):
    """????????????????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    serializer_class = MthAdjustLineSerializer
    # queryset= MthAdjustLine.objects.all()
    renderer_classes = (XLSXRenderer,)
    filename = '?????????????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    # filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_queryset(self):
        id = self.request.query_params.get("id")
        mthadjust = MthAdjust.objects.get(pk=id)
        self.mthadjust = mthadjust
        return mthadjust.mthadjustline_set.all().order_by("customer_id")

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 

    def get_header(self):
        header_title = "{}{}?????????????????????".format(self.mthadjust.organization.name,self.mthadjust.mth)
        header = {
            'tab_title': "??????????????????",
            'header_title': header_title,
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
        return header

class MthDraftCustomerBillExportViewSet(XLSXFileMixin, ListAPIView):
    """??????????????????????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    serializer_class = MthDraftCustomerBillLineSerializer
    # queryset= MthAdjustLine.objects.all()
    renderer_classes = (XLSXRenderer,)
    filename = '????????????????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    # filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_queryset(self):
        id = self.request.query_params.get("id")
        mthdraftcustomerbill= MthDraftCustomerBill.objects.get(pk=id)
        self.mthdraftcustomerbill= mthdraftcustomerbill
        return mthdraftcustomerbill.mthdraftcustomerbillline_set.all().order_by("customer_id")

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 

    def get_header(self):
        header_title = "{}{}????????????????????????".format(self.mthdraftcustomerbill.organization.name,self.mthdraftcustomerbill.mth)
        header = {
            'tab_title': "????????????????????????",
            'header_title': header_title,
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
        return header

class MthCustomerBillExportViewSet(XLSXFileMixin, ListAPIView):
    """???????????????????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    serializer_class = MthCustomerBillLineSerializer
    # queryset= MthAdjustLine.objects.all()
    renderer_classes = (XLSXRenderer,)
    filename = '?????????????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    # filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_queryset(self):
        id = self.request.query_params.get("id")
        mthcustomerbill= MthCustomerBill.objects.get(pk=id)
        self.mthcustomerbill= mthcustomerbill
        return mthcustomerbill.mthcustomerbillline_set.all().order_by("customer_id")

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 

    def get_header(self):
        header_title = "{}{}?????????????????????".format(self.mthcustomerbill.organization.name,self.mthcustomerbill.mth)
        header = {
            'tab_title': "?????????????????????",
            'header_title': header_title,
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
        return header

class MthAgentBillExportViewSet(XLSXFileMixin, ListAPIView):
    """?????????????????????

    Args:
        XLSXFileMixin (_type_): _description_
        ListAPIView (_type_): _description_
    """
    permission_classes = (AllowAny,)
    xlsx_use_labels = True
    xlsx_boolean_labels = {True: "???", False: "???"}
    serializer_class = MthAgentBillLineSerializer
    # queryset= MthAdjustLine.objects.all()
    renderer_classes = (XLSXRenderer,)
    filename = '?????????????????????.xlsx' 
    xlsx_ignore_headers = ["id"]
    # filterset_fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact","in"]} 

    def get_queryset(self):
        id = self.request.query_params.get("id")
        mthagentbill= MthAgentBill.objects.get(pk=id)
        self.mthagentbill= mthagentbill
        return mthagentbill.mthagentbillline_set.all().order_by("agent_id")

    def get_body(self):
        return body

    def get_column_header(self):
        return column_header 

    def get_header(self):
        header_title = "{}{}?????????????????????".format(self.mthagentbill.organization.name,self.mthagentbill.mth)
        header = {
            'tab_title': "?????????????????????",
            'header_title': header_title,
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
        return header