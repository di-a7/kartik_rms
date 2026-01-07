from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, OrderItem
from .serializers import CategorySerializer
from rest_framework import status
# Create your views here.
# Class Based

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CategoryAPIView(ListCreateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def destroy(self, request, *args, **kwargs):
      category = self.get_object()
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Protected: Category can't be deleted. Related to OrderItem"})
      category.delete()
      return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)







# APIView
# from rest_framework.views import APIView

# class CategoryList(APIView):
#    def get(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def post(self, request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail": "New data created", "data": serializer.data}, status = status.HTTP_201_CREATED)


# class CategoryDetail(APIView):
#    def get(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def put(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category , data = request.data) 
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail": "Data edited", "data": serializer.data})
   
#    def delete(self, request, id):
#       category = Category.objects.get(id = id)
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)
      







# Function based 
# @api_view(['GET','POST'])
# def category_list(request):
#    if request.method == "GET":
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)  # serializetion: object is converted to json
#       return Response(serializer.data)
   
#    elif request.method == "POST":
#       serializer = CategorySerializer(data = request.data)  # deserializer: json is converted to object
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail": "New data created", "data": serializer.data}, status = status.HTTP_201_CREATED)


# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,id):
#    category = Category.objects.get(id = id)
   
#    if request.method == "GET":
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == "PUT": 
#       serializer = CategorySerializer(category , data = request.data) 
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail": "Data edited", "data": serializer.data})
   
#    elif request.method == "DELETE":
#       category.delete()
#       return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)