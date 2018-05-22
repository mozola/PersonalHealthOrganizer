from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercises

def single_exercise(exercise_type):
    exercises_type = {}
    index = 1
    index_2 = 1
    simple_list = []

    for exercise in Exercises.objects.filter(exercise_type=exercise_type):
        if index % 3 != 0:
            simple_list.append(exercise)

        else:
            simple_list.append(exercise)
            exercises_type[index_2] = simple_list
            simple_list = []
            index_2 = index_2 + 1

        index = index + 1

    return exercises_type


def index(request):
    return render(request, 'exercises/index.html',
                  {
                      'headers': single_exercise('headers'),
                      'biceps': single_exercise('biceps'),
                      'triceps': single_exercise('triceps'),
                      'stomag': single_exercise('stomag'),
                      'chest': single_exercise('chest'),
                      'thigs': single_exercise('thigs'),
                      'crossbones': single_exercise('crossbones')
                  })
