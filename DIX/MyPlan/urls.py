# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^new_plan', views.new_plan, name = 'new_plan'),
    url(r'^all', views.my_plans, name='my_plans'),
]