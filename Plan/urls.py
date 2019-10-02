from django.urls import path
from . import views

urlpatterns = [
    path('new_plan/', views.CreatePlan.as_view(), name='new_plan'),
    path('new_plan_day/', views.CreatePlanDay.as_view(), name='new_plan_day'),
    path('all', views.my_plans, name='my_plans_all'),
    path('my_plans/<int:plan_id>', views.plan_start_stop, name='start-sprint'),
    path('day-plan/<int:plan_id>/detail/', views.details_single_plan, name='detail_meal'),
]
