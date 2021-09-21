"""evrekaDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from navigationrecord.views import front, get_two_days_data, homepage
from binoperations.views import opfront, bins_operations_pair

urlpatterns = [
    path('', homepage, name='homepage'),
    path('twodays/', get_two_days_data, name='twodaysdata'),
    path('front/', front, name='front'),
    path('opfront/', opfront, name='opfront'),
    path('binoppair/', bins_operations_pair, name='binoppair'),
    path('admin/', admin.site.urls),
]
