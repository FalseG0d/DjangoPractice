from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    #path('request',views.make_request,name="make_request"),
    path('register',views.register,name="register"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),


    path('rest_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset_password"),
    path('rest_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_done"),
    path('rest/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_confirm"),
    path('rest_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name="password_reset_complete"),

]
