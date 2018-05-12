# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import date

from rest_framework import generics

from employee_app.serializers import EmpSerializer
from .models import Employee
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)


@api_view(['GET'])
def details(request, pk):
    employee = Employee.objects.get(pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        address = request.POST['address']
        position = request.POST['position']
        hireDate = request.POST['hireDate']

        if hireDate is '':
            hireDate = date.today()
        if age is '':
            age = 0
        employee = Employee(name=name, age=age, email=email, address=address,
                            position=position, hireDate=hireDate)
        employee.save()

        return redirect('/empls')
    else:
        return render(request, 'add.html')


class EmpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
