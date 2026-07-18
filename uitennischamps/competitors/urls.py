"""uitennischamps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from competitors import views

from django.http import HttpResponse
from django.template import loader

urlpatterns =[
    path('',views.index_view, name= 'index'),
    path('admin/', admin.site.urls),
    path('index/', views.index_view, name= 'index'),
    path('matches/', views.match_view, name= 'matches'),
    path('player/', views.player_view, name= 'player'),
    path('biodata/', views.biodata_form, name= 'biodata'),
    path('match_detail/', views.match_detail_view, name= 'match_detail'),
    path('base/', views.base_view, name= 'base'),   
    path('contact_view/', views.contact_view, name = 'contact'),
    ]