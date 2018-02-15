# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import date
from dateutil.relativedelta import relativedelta

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
        dt_list = hireDate.split('-')
        experience = ''
        if hireDate is not '':
            d1 = date(int(dt_list[0]), int(dt_list[1]), int(dt_list[2]))
            d2 = date.today()
            rdelta = relativedelta(d2, d1)
            if rdelta.years is not 0:
                experience = experience + str(rdelta.years) + ' y, '
            if rdelta.months is not 0:
                experience = experience + str(rdelta.months) + ' m, '
            experience = experience + str(rdelta.days) + ' d'
        else:
            hireDate = date.today()
            experience = experience + '0 d'

        if age is '':
            age = 0
        employee = Employee(name=name, age=age, email=email, address=address,
                            position=position, hireDate=hireDate, experience=experience)
        employee.save()

        return redirect('/empls')
    else:
        return render(request, 'add.html')
