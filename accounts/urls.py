from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    path('reset/(<uidb64>[0-9A-Za-z_\-])/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView, name='change_password'),
]