# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:22:12 2014

@author: jkr
"""

from django import template

register = template.Library()

@register.filter
def lookup(value, arg):
    return value[arg]