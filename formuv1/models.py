#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:02:49 2020

@author: vanderneto
"""

from django.db import models


class Order(models.Model):
    URL = models.CharField(max_length=250)


class ItemOrder(models.Model):
    order = models.ForeignKey('Order',on_delete=models.CASCADE)
    URL = models.CharField(max_length=250)
    #product = models.CharField(max_length=250)
    #quantity = models.PositiveIntegerField()
    #price = models.DecimalField(max_digits=20, decimal_places=2)