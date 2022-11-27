# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:58:41 2022

@author: TMH
"""

from django.urls import path 
from.views import HomePageView, AboutPageView
urlpatterns = [
    path ('about/',AboutPageView.as_view(),name='about'),
    path ('',HomePageView.as_view(),name='home'),
    ]