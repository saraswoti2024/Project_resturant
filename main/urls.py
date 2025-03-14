from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


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
    path('change_password/',change_password,name="change_password"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/login"), name='password_reset_complete'),
]