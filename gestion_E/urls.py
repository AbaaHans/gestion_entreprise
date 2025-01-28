from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from crm import views as crm_views
from produit import views as product_views
from finance import view as finance_views
from suppliers import views as suppliers_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    # API endpoints
    path('api/', include('api.urls')),
    
    # CRM
    path('clients/', crm_views.client_list, name='client_list'),
    path('clients/create/', crm_views.client_create, name='client_create'),
    path('clients/<int:pk>/', crm_views.client_detail, name='client_detail'),
    path('clients/<int:pk>/update/', crm_views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', crm_views.client_delete, name='client_delete'),
    
    # Products
    path('products/', product_views.product_list, name='product_list'),
    path('products/create/', product_views.product_create, name='product_create'),
    path('products/<int:pk>/', product_views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', product_views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_views.product_delete, name='product_delete'),

    #Service
    path('services/', product_views.service_list, name='service_list'),
    path('services/create/', product_views.service_create, name='service_create'),
    path('services/<int:pk>/', product_views.service_detail, name='service_detail'),
    path('services/<int:pk>/update/', product_views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', product_views.service_delete, name='service_delete'),
    
   
     # Finance
    path('finance/', include('finance.urls')),  # Inclure toutes les URLs finance


    # Fournisseur
    path('suppliers/', suppliers_views.supplier_list, name='supplier_list'),
    path('suppliers/create/', suppliers_views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/', suppliers_views.supplier_detail, name='supplier_detail'),
    path('suppliers/<int:pk>/update/', suppliers_views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', suppliers_views.supplier_delete, name='supplier_delete'),
]


