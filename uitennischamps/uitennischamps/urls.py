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
from competitors import views as competitors_views

urlpatterns = [
    path('',competitors_views.index_view, name = 'index'),
    path('admin/', admin.site.urls),
    path('index/', competitors_views.index_view, name = 'index'),
    path('matches/', competitors_views.match_view, name = 'matches'),
    path('player/', competitors_views.player_view, name= 'player'),
    path('biodata/', competitors_views.biodata_form, name= 'biodata'),
    path('match_details/', competitors_views.match_details_view, name= 'match_details'),
    path('base/', competitors_views.base_view, name= 'base'),   
    path('score_view/', competitors_views.score_view, name = 'score'),
    path('contact/', competitors_views.contact_form, name= 'contact'),
    path('signin/', competitors_views.signin_view, name= 'signin'),
    path('signup/', competitors_views.signup_view, name= 'signup'),
]
    # other paths can be added here   
    #path('base/', views.base_view, name = 'base')
    # path('apps/', )
