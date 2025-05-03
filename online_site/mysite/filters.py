from django_filters import FilterSet
from .models import  Clothes

class ClothesFilter(FilterSet):
    class Meta:
        model = Clothes
        fields = {
        'category':['exact'],
        'prise':['gt','lt']
        }