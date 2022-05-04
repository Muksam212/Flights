from django.contrib import admin
from .import views
from django.urls import path

app_name = "main" #custom url which is very important
urlpatterns = [
	path('', views.homepage, name="p"),
	path('<int:id>/', views.flight, name="flights"),
	path('<int:id>/book', views.book, name="book")
]