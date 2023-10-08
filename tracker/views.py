from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "tracker/dashboard.html")
    
def loginview(request):
    return render(request, "tracker/login.html")

def loginauth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("dashboard")
    else:
        return HttpResponse("Invalid Credentials")
    
def logoutreq(request):
    logout(request)
    return redirect("index")