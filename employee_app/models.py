# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.TextField()
    position = models.CharField(max_length=200)
    hireDate = models.DateField(default=timezone.now, blank=True)
    experience = models.CharField(max_length=200)

    def __str__(self):
        return self.name

