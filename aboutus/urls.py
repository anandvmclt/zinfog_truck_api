#Aboutus/urls.py
from django.urls import path,include
from .views import AboutAPIView
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="Home"),
    path('about/', AboutAPIView.as_view(), name="AboutUS")
]
