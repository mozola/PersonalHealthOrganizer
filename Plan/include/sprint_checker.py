#!coding=utf-8
import datetime
from .models import Sprints

class SprintChecker(object):
    def __init__(self, Sprints):
        pass

    def check_actual_sprint(self):
        for single_plan in Sprints.objects.get(sprint_status == 'Nowy'):
            if single_plan.plan_date == datetime.date:
                return single_plan
            else:
                pass


    def get_new_sprint(self):
        if self.check_actual_sprint().sprint_status is 'Nowy':
            pass

        else:
            print('Actually you have started sprint')
