# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/', views.index, name = 'index'),
    url(r'^new_meal/', views.new_meal, name = 'new_meal'),
    #url adress with some value
    url(r'^(?P<meal_id>[0-9]+)$', views.details, name = 'details')

]

