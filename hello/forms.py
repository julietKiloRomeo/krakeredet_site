# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 20:56:40 2014

@author: jkr
"""

from hello.models import Profile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'birthdate')