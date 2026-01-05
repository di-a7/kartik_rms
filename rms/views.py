from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from rest_framework import status
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
      return Response({"detail": "New data created", "data": serializer.data}, status = status.HTTP_201_CREATED)


@api_view(['GET','DELETE','PUT'])
def category_detail(request,id):
   category = Category.objects.get(id = id)
   
   if request.method == "GET":
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   
   elif request.method == "PUT": 
      serializer = CategorySerializer(category , data = request.data) 
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"detail": "Data edited", "data": serializer.data})
   
   elif request.method == "DELETE":
      category.delete()
      return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)