from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id','name']

admin.site.register(Food)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
   list_display = ['number','capacity','avaiable']
   list_filter = ['capacity','avaiable']
   list_editable = ['avaiable']

admin.site.register(Order)
admin.site.register(OrderItem)   