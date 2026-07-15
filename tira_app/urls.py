from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('category/<str:name>', views.category, name='category'),
        path('singal_product/<int:product_id>', views.singal_product, name='singal_product'),
        path('login', views.login_user, name='login_user'),   
        path('logout', views.logout_user, name='logout_user'),     
        path('register', views.register, name='register'),
]