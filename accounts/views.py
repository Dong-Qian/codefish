from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.urls import reverse

from .forms import UserLoginForm

# Create your views here.

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # save user in session
        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('home'))

    context = {
        "login_form": form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



