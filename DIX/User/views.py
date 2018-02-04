from django.shortcuts import render
from django.http import HttpResponse
from forms import UserForm
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'user/output.html', {'result': 'Gratulacje\n udalo ci sie zalogowac.'})
        else:
            return render(request, 'user/output.html', {'result': 'Jestes juz zalogowany'})

    return render(request, 'user/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'user/output.html', {'result': 'Wylogowales sie'})


def register(request):
    #if request.POST:
        #form = UserForm(request.POST)
        #if form.is_valid():
        #    #form = form.save()
        #    return render(request, 'user/output.html', {'result': 'Udalo sie'})
        #else:
        #    form = UserForm()
    return render(request, 'user/register.html')