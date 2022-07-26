from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('catalog/', views.catalogPage, name='catalogPage'),
    path('catalog/<int:pk>/', views.productPage, name='productPage'),
]