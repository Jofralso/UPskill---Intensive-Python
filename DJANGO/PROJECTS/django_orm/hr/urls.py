from django.urls import path
from . import views

urlpatterns = [
    path('hr/<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
