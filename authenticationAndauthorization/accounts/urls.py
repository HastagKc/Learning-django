from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import user_login, user_logout, user_register, dashboard
# from accounts.views import user_login, user_logout ,user_register, dashboard
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Password Reset URLs
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="accounts/forgetpass/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/forgetpass/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/forgetpass/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/forgetpass/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]



