from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView
urlpatterns = [
   path('category/',CategoryAPIView.as_view()),
   path('category/<pk>/',CategoryDetailAPIView.as_view())
]
