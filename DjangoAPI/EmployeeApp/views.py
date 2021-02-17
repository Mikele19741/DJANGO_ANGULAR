from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Departments, Employees
from django.http.response import JsonResponse

from .serialazer import DepartmentSerialazer, EmployeesSerialazer

@csrf_exempt
def departmentAPI(request, id=0):
    if request.method=='GET':
        departments=Departments.objects.all()
        department_serializer=DepartmentSerialazer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerialazer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successful!!!", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerialazer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successful!!!", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('Department deleted', safe=False)
@csrf_exempt
def employeAPI(request, id=0):
    if request.method=='GET':
        employees=Employees.objects.all()
        employees_serializer=EmployeesSerialazer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=DepartmentSerialazer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successful!!!", safe=False)
        return JsonResponse('Failed to Add employee', safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(DepartmentId=employee_data['DepartmentId'])
        employee_serializer=DepartmentSerialazer(employee, data=employee_data)
        if  employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successful!!!", safe=False)
        return JsonResponse('Failed to Add employee', safe=False)
    elif request.method=='DELETE':
        employee=Employees.objects.get(DepartmentId=id)
        employee.delete()
        return JsonResponse('Employee deleted', safe=False)





