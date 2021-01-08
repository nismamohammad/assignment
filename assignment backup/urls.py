"""project URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),

    path('admin_users_view', views.admin_users_view, name='admin_users_view'),

    path('user_registration', views.user_registration, name='user_registration'),
    path('user_login', views.user_validation, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),
    path('user_logout', views.user_logout, name='user_logout'),

    path('user_pic_pool_add', views.user_pic_pool_add, name='user_pic_pool_add'),
    path('user_pic_pool_view', views.user_pic_pool_view, name='user_pic_pool_view'),
    path('user_pic_pool_delete', views.user_pic_pool_delete, name='user_pic_pool_delete'),

]
