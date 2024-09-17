from django_filters import rest_framework as filters
from  magazin.models import Category,Product

class ProductFilter(filters.FilterSet):
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price_gte', 'price_lte', 'category']


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', 'description']
