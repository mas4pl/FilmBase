from django.urls import path
from . import views

urlpatterns = [
      path('login/', views.user_login, name='login'),
      path('filldb', views.filldb, name='filldb'),
]
