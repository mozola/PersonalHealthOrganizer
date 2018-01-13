from django.shortcuts import render
from django.http import HttpResponse
from forms import UserForm


def login(request):
    return render(request, 'user/login.html')


def logout(request):
    return render(request, 'user/output.html', {'result': 'Wylogowales sie'})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #form = form.save()
            return render(request, 'user/output.html', {'result': 'Udalo sie'})
        else:
            form = UserForm()
            return render(request, 'user/register.html', {'form': form})