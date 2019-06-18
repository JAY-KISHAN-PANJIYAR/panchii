# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:51:37 2019

@author: user
"""


from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
]
