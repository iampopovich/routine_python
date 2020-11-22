"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from response_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    re_path(r'^products/$', views.products),
    re_path(r'path', views.regular_middleware, name='reg_url'),
    re_path(r'^products/phones|tablets/', views.gadgets, name='gadgets'),
    path('products/<int:product_id>/', views.products),
    re_path(r'^users/(?P<user_id>\d+)/(?P<user_name>\D+)/', views.users),
    path('users/', views.users)
]