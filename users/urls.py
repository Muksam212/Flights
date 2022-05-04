from django.contrib import admin
from django.urls import path
from users import views

app_name = "users" #custom url

urlpatterns = [
	path('login/', views.login_view, name="login_users"),
	path('logout/', views.logout_view, name="logout_users"),
	path('user', views.index, name='index')

]