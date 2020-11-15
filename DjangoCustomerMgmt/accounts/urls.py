from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),

    path('account/',views.accountSettings,name='account'),

    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('user/', views.userPage, name="user-page"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('rest_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset_password"),
    path('rest_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_done"),
    path('rest/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_confirm"),
    path('rest_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name="password_reset_complete"),

]