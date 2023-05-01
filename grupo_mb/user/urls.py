from django.urls import path
from .views import UserCreateView, UserListView, UserListViewByAge, UserListViewByLastName, UserUpdateView, UserDeleteView

urlpatterns = [
    path('usuario/', UserCreateView.as_view()),
    path('usuario/todos/', UserListView.as_view()),
    path('usuario/edad/', UserListViewByAge.as_view()),
    path('usuario/apellido_paterno/', UserListViewByLastName.as_view()),
    path('usuario/<int:pk>/', UserUpdateView.as_view()),
    path('usuario/<int:pk>/delete/', UserDeleteView.as_view()),
]
