from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Category(models.Model):
   name = models.CharField(max_length=100)
   
   def __str__(self):
      return self.name
class Food(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.IntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   def __str__(self):
      return self.name

class Table(models.Model):
   number = models.CharField(max_length=1)
   capacity = models.IntegerField()
   avaiable = models.BooleanField(default=False)
   def __str__(self):
      return f"Table {self.number}"

class Order(models.Model):
   PENDING = "P"
   COMPLETE = "C"
   DELIVERED = "D"
   STATUS_CHOICES = [
      (PENDING , "Pending"),
      (COMPLETE, "Complete"),
      (DELIVERED, "Delivered")
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   table = models.ForeignKey(Table, on_delete=models.CASCADE,null=True, blank=True)
   total_price = models.IntegerField(null=True, blank=True)
   status = models.CharField(max_length=1, choices=STATUS_CHOICES, default = PENDING)
   payment_status = models.BooleanField(default = False)
   
   def __str__(self):
      return f"{self.user} - {self.table}"


class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)