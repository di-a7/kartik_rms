from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   
   def create(self, validated_data):
      category = Category.objects.create(name = validated_data.get('name'))
      # Category.objects.create(**validated_data)
      return category
   
   def update(self, instance, validated_data):        # validated_data = {"name":"drinks"}
      instance.name = validated_data.get('name', instance.name)
      instance.save()
      return instance
   
   

# instance = Todo.objects.get(id = 1)
# instance.title # print the title of id 1
# instance.title = "new title"
# instance.save()