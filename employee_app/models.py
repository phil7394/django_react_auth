# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your models here.


class Employee(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.TextField()
    position = models.CharField(max_length=200)
    hireDate = models.DateField(default=timezone.now, blank=True)

    @property
    def experience(self):
        experience = ''
        d1 = self.hireDate
        d2 = date.today()
        rdelta = relativedelta(d2, d1)
        if rdelta.years is not 0:
            experience = experience + str(rdelta.years) + ' y, '
        if rdelta.months is not 0:
            experience = experience + str(rdelta.months) + ' m, '
        experience = experience + str(rdelta.days) + ' d'
        return experience

    def __str__(self):
        return self.name

