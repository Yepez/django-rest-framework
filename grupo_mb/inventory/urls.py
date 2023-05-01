from django.urls import path
from . import views

urlpatterns = [
    path('inventarios/', views.InventoryList.as_view(), name='inventory-list'),
    path('inventarios/<int:pk>/', views.InventoryDetail.as_view(), name='inventory-detail'),
]
