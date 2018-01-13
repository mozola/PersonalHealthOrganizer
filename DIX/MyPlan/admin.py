# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SinglePlan
from .models import Sprints

admin.site.register(SinglePlan)
admin.site.register(Sprints)
