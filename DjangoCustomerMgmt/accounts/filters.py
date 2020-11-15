import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    date_created=DateFilter(field_name="date_created",lookup_expr="gte")
    due_date=DateFilter(field_name="due_date",lookup_expr="lte")
    note=CharFilter(field_name='note',lookup_expr="icontains")
    
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','date_created','due_date']