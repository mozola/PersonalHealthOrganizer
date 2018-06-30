# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Meal
from .models import Product
from .models import Component

class MealAdmin(admin.ModelAdmin):
    list_display = ['name',  'types']
    list_filter = ['name', 'types']
    search_fields = ['name']
    ordering = ['name']


class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['component', 'count', 'units']


admin.site.register(Meal, MealAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Product, ProductAdmin)
