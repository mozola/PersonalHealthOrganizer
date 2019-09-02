from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new_plan/', views.CreatePlan.as_view(), name = 'new_plan'),
    url(r'^new_plan_day/', views.CreatePlanDay.as_view(), name = 'new_plan_day'),
    url(r'^my_plans', views.my_plans, name='my_plans'),
    url(r'^all', views.my_plans, name='my_plans_all'),
    url(r'^start-sprint', views.start_sprint, name='start-sprint'),
]