#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:02:49 2020

@author: vanderneto
"""

from django.db import models


class Order(models.Model):
    client = models.CharField()
    date = models.DateField(auto_now_add=True)


class ItemOrder(models.Model):
    order = models.ForeignKey('Order')
    product = models.CharField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)