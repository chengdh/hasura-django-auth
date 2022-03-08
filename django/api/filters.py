from django_filters import rest_framework as filters
from .models import Role,HasuraUser
class BooleanInFilter(filters.BaseInFilter, filters.BooleanFilter):
    pass

class RoleFilter(filters.FilterSet):
    is_active__in = BooleanInFilter(field_name='is_active', lookup_expr='in')

    class Meta:
        model = Role 
        fields = {"name": ["exact","iexact","contains","icontains"],"is_active": ["exact"]} 

