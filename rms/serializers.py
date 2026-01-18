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
   items = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only=True)
   payment_status = serializers.BooleanField(read_only=True)
   total_price = serializers.IntegerField(read_only=True)
   class Meta:
      model = Order
      fields = ["user","table","total_price","status","payment_status","items"]
   
   def create(self, validated_data):
      items =  validated_data.pop('items')      #"items": [{"food": 1},{"food": 22},{"food": 22},{"food": 22}]
      total = 0
      for item in items:
         food_item = item.get('food')     # food_item = 1
         total += food_item.price
      
      order = Order.objects.create(total_price = total, **validated_data)
      for item in items:
         OrderItem.objects.create(order = order, food = item.get('food'))
      return order





# data optimization, filtering, pagination

#{
#   "total_price": 500,
#   
# }

# 

