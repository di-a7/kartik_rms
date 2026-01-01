from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id','name']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
   list_display = ['number','capacity','avaiable']
   list_filter = ['capacity','avaiable']
   list_editable = ['avaiable']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
   list_display = ['name','description','price','category']
   list_filter = ['category']
   search_fields = ['name']


# class OrderItemInline(admin.StackedInline):
class OrderItemInline(admin.TabularInline):
   model = OrderItem
   autocomplete_fields = ['food']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','user','table','total_price','status','payment_status']
   list_filter = ['status','payment_status']
   search_fields = ['user__username','table__number']
   inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
   list_display = ['order','food']
   search_fields = ['food__name']