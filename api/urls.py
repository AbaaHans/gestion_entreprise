from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
]