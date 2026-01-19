from django.urls import path
from .views import *

urlpatterns = [
   path('login/',LoginAPIView.as_view()),
   path('set-session',set_session),
   path('get-session',get_session),
   path('delete-session',delete_session)
]
