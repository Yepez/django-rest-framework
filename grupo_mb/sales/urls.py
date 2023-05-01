from django.urls import path
from .views import SaleListCreateView, SaleRetrieveUpdateDestroyView, SalesByDateView, SalesByEmployeeView

urlpatterns = [
    path('ventas/', SaleListCreateView.as_view(), name='sales-list-create'),
    path('ventas/<int:pk>/', SaleRetrieveUpdateDestroyView.as_view(), name='sales-retrieve-update-destroy'),
    path('ventas/por-fecha/', SalesByDateView.as_view(), name='sales-by-date'),
    path('ventas/por-empleado/', SalesByEmployeeView.as_view(), name='sales-by-employee'),
]