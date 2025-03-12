from django.urls import path
from .views import *


# app_name = 'main'
urlpatterns = [
    path('',home,name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('menu/',menu,name="menu"),
    path('services/',services,name="services"),
    path('login/',log_in,name="login"),
    path('register/',register,name="register"),
    path('Terms/',Terms,name="Terms"),
    path('privacy/',privacy,name="privacy"),
    path('services/',services,name="services"),
    path('policy/',policy,name="policy"),
    path('support/',support,name="support"),
    path('logout/',log_out,name="logout"),
    path('change_password/',change_password,name="change_password")
]
