
from .models import Departments, Employees
from rest_framework import serializers, viewsets, routers

class DepartmentSerialazer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId',
                'DepartmentName')

class EmployeesSerialazer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId',
                'EmployeeName',
                'Department',
                'DateOfJoing',
                'PjotoFileName')