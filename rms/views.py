from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filter import FoodFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
# Create your views here.
# Class Based
# ModelViewset

@extend_schema(tags=['Category'])
class CategoryViewset(viewsets.ReadOnlyModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticatedOrReadOnly]
   
   @extend_schema(
      parameters=[
         OpenApiParameter(name='name', description='Name of the food', required=False, type=str),
      ],
      description='This is a GET food api',
   )
   def list(self, request):
      # your non-standard behaviour
      return super().list(request)
   
   def destroy(self, request, pk):
      category = self.get_object()
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Protected: Category can't be deleted. Related to OrderItem"})
      category.delete()
      return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)

@extend_schema(tags=['Foods'])
class FoodViewset(viewsets.ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   filter_backends = [filters.SearchFilter, DjangoFilterBackend]
   search_fields = ['name']
   filterset_fields  = ['category']
   filterset_class = FoodFilter
   permission_classes = [IsAuthenticatedOrReadOnly]
   
   @extend_schema(
      parameters=[
         OpenApiParameter(name='description', description='Name of the food', required=False, type=str),
      ],
      description='This is a GET food api',
   )
   def list(self, request):
      # your non-standard behaviour
      return super().list(request)

@extend_schema(tags=['Orders'])
class OrderViewset(viewsets.ModelViewSet):
   queryset = Order.objects.prefetch_related('items').all()
   serializer_class = OrderSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]
   pagination_class = PageNumberPagination




# Viewset
# class CategoryViewset(viewsets.ViewSet):
#    def list(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def create(self, request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail": "New data created", "data": serializer.data}, status = status.HTTP_201_CREATED)

# class CategoryDetailViewset(viewsets.ViewSet):
#    def retrieve(self, request, pk):
#       category = Category.objects.get(pk = pk)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)



# # Generic with Mixins
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class CategoryAPIView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def destroy(self, request, *args, **kwargs):
#       category = self.get_object()
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has been deleted."}, status = status.HTTP_204_NO_CONTENT)







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