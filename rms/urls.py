from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category',CategoryViewset, basename='category')
router.register('foods', FoodViewset, basename='foods')
router.register('orders', OrderViewset, basename='orders')

urlpatterns = [
   # path('category/',CategoryViewset.as_view({'get':'list','post':'create'})),
   # path('category/<pk>/',CategoryViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
] + router.urls
