# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Employees'
