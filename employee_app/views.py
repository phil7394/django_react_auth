# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees

# Create your views here.


def index(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)


def details(request, id):
    employee = Employees.objects.get(id=id)
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

        employee = Employees(name=name, age=age, email=email, address=address)
        employee.save()

        return redirect('/empls')
    else:
        return render(request, 'add.html')

