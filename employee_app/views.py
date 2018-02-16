# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import date


from .models import Employee

# Create your views here.


def index(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)


def details(request, id):
    employee = Employee.objects.get(id=id)
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
