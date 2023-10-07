from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tracker index.")

def dashboard(request):
    return HttpResponse("Hello, world. You're at the tracker dashboard.")

def login(request):
    return render(request, "tracker/login.html")

def loginauth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        
    else:
        return HttpResponse("Invalid Credentials")
    
def logoutreq(request):
    logout(request)
    redirect("index")