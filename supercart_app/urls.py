from django.urls import path
from supercart_app import views

urlpatterns = [
    path("", views.home, name="home"),
]