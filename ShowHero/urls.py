"""ShowInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from ShowInfo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hobby/',say_hobby),
    path('app_for/',app_for),
    path('nav/',nav),
    path('login/',login),
    path('login_s/',login_s),
    path('filter/',filter),
    path('getTemplate/',getTemplate),
    re_path('^$',imgs),
    path('hero/',hero)
]
