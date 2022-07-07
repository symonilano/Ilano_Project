"""Ilano_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Ilano_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomePage, name="home"),
    path('about/', AboutPage, name="about"),
    path('seller/', SellerPage, name="seller"),
    path('sell/', SellPage, name="sell"),
    path('order/', OrderPage, name="order"),
    path('delivery/', DeliveryPage, name="delivery"),

    path('add-seller/', AddSeller, name="add-seller"),
    path('update-seller/<str:pk>/', UpdateSeller, name="update-seller"),
    path('delete-seller/<str:pk>/', DeleteSeller, name="delete-seller"),

    path('add-sell/', AddSell, name="add-sell"),
    path('update-sell/<str:pk>/', UpdateSell, name="update-sell"),
    path('delete-sell/<str:pk>/', DeleteSell, name="delete-sell"),

    path('add-order/', AddOrder, name="add-order"),
    path('update-order/<str:pk>/', UpdateOrder, name="update-order"),
    path('delete-order/<str:pk>/', DeleteOrder, name="delete-order"),

    path('add-delivery/', AddDelivery, name="add-delivery"),
    path('update-delivery/<str:pk>/', UpdateDelivery, name="update-delivery"),
    path('delete-delivery/<str:pk>/', DeleteDelivery, name="delete-delivery"),

    path('add-review/', AddReview, name="add-review"),
    path('review/', ReviewPage, name="review"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
