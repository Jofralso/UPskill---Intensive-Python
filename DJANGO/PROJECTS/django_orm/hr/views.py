from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee_detail.html', {'employee':employee})