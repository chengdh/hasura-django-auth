from django.urls import path
from .export_views import CustomerExportViewSet,AgentExportViewSet,ContractExportViewSet,MthAdjustExportViewSet,MthDraftCustomerBillExportViewSet,MthCustomerBillExportViewSet,MthAgentBillExportViewSet
urlpatterns = [
    path('export_electric_power_sale_customer/', CustomerExportViewSet.as_view(), name='export_customer'),
    path('export_electric_power_sale_agent/', AgentExportViewSet.as_view(), name='export_agent'),
    path('export_electric_power_sale_contract/', ContractExportViewSet.as_view(), name='export_contract'),
    path('export_electric_power_sale_mthadjust/', MthAdjustExportViewSet.as_view(), name='export_mthadjust'),
    path('export_electric_power_sale_mthdraftcustomerbill/', MthDraftCustomerBillExportViewSet.as_view(), name='export_mthdraftcustomerbill'),
    path('export_electric_power_sale_mthcustomerbill/', MthCustomerBillExportViewSet.as_view(), name='export_mthcustomerbill'),
    path('export_electric_power_sale_mthagentbill/', MthAgentBillExportViewSet.as_view(), name='export_mthagentbill'),
]