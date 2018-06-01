"""movierecomend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from movie import views
urlpatterns = [
    path('', views.index,name='index'),
    path('single/<int:id>/', views.single,name='single'),
    path('admin/', admin.site.urls),
    path('login/', views.rlogin, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.rlogout, name="logout"),
    
]

admin.site.site_header = '推荐系统后台管理';
admin.site.index_title = '首页-推荐系统';
admin.site.site_title = '推荐系统';