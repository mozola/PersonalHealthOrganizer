from django.contrib import admin
from .models import Meal
from .models import Product
from .models import Component


class MealAdmin(admin.ModelAdmin):
    list_display = ['name',  'types', 'callories']
    list_filter = ['name', 'types']
    search_fields = ['name']
    ordering = ['name']


class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'waste', 'units']
    search_fields = ['name']
    ordering = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['component', 'count', 'units', 'calories']


admin.site.register(Meal, MealAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Product, ProductAdmin)
