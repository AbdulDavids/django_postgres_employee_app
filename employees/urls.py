from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]
