from django.urls import path
from . import views

urlpatterns = [
    path('', views.store,name="services"),
    path('<str:pk>/', views.service,name="service"),
    path('type/<str:pk>', views.all_service,name="view_all"),
]
