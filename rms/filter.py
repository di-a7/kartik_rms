from django_filters import FilterSet
from .models import Food

class FoodFilter(FilterSet):
   class Meta:
      model = Food
      fields ={
         'price': ['lt', 'gt'],
         'category': ['exact'],
      }
