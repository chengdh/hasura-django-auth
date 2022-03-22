from django.urls import path
from .export_views import CustomerExportViewSet
urlpatterns = [
    path('export_electric_power_sale_customer/', CustomerExportViewSet.as_view(), name='export_customer'),
]