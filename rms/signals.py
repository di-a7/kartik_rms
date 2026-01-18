from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender=Order)
def notify(sender, instance, created, **kwargs):
   print(f"Order {instance.id} has been created.")
   send_mail(
      "Order Created!",
      "Your order has been created Successfully.",
      "demo@example.com",
      ["diya@gmail.com"],
      fail_silently=False
   )