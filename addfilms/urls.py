from django.urls import path
from . import views

urlpatterns = [
      path('login/', views.user_login, name='login'),
      path('filldb', views.filldb, name='filldb'),
      path('filldb2', views.filldb2, name='filldb2'),
      path('filldb3', views.filldb3, name='filldb3'),
]
