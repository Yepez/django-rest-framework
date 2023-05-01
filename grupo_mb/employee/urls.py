from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('empleados/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('empleados/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
]