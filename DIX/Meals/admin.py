# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Meals
from .models import Components

admin.site.register(Meals)
admin.site.register(Components)
