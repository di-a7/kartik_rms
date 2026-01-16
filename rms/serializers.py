from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']
      # exclude = ['name']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      category = Category.objects.filter(name = validated_data.get('name')).count()
      if category > 0:
         raise serializers.ValidationError({"details":"This category already exists."})
      return super().save(**kwargs)



class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   # category = serializers.StringRelatedField()
   # category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   class Meta:
      model = Food
      fields = ['id','name','description','price','price_with_tax','category']
   
   def get_price_with_tax(self, food:Food):
      return food.price * 0.11 + food.price

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['food']


class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer()
   class Meta:
      model = Order
      fields = ["user","table","total_price","status","payment_status","items"]
# data optimization, filtering, pagination





