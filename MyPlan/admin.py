# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SinglePlan
from .models import Sprints


class SprintAdmin(admin.ModelAdmin):
    list_display = ['sprint_name', 'sprint_status']
    list_filter = ['sprint_name', 'sprint_status']
    ordering = ['sprint_name']


class SingleAdmin(admin.ModelAdmin):
    list_display = ['plan_date', 'state']
    list_filter = ['plan_date', 'state']
    ordering = ['plan_date']


admin.site.register(SinglePlan, SingleAdmin)
admin.site.register(Sprints, SprintAdmin)
