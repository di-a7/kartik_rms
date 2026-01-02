from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
@api_view(['GET','POST'])
def category_list(request):
   if request.method == "GET":
      category = Category.objects.all()
      serializer = CategorySerializer(category, many=True)  # serializetion: object is converted to json
      return Response(serializer.data)
   elif request.method == "POST":
      serializer = CategorySerializer(data = request.data)  # deserializer: json is converted to object
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"detail": "New data created", "data": serializer.data})


