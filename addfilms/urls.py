from django.urls import path
from . import views

urlpatterns = [
      path('home', views.home, name='home'),
      path('login', views.user_login, name='login'),
      path('filldb', views.filldb, name='filldb'),
      path('view_all', views.view_all, name='view_all'),
      path('user_aut', views.user_aut, name='user_aut'),
]
