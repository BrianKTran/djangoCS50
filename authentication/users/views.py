from django.contrib.auth import authentication, login, logout
from django.shortcuts import render
from django.http import HttpResponse, httpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authentication(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return httpResponseRedirect(reverse("Index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return redner(request, "users/login.html", {"message": "Logged out."})
