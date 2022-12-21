from django.shortcuts import render,redirect
from .form import signinform
from django.contrib.auth import authenticate, login
# Create your views here.

def signinview(request):
    if request.method=="post":
        form = signinform(request.POST)
        if form.is_valid():
            form.save
            return redirect('login')
    else:
        form = signinform()
        return render(request,"signin.html",{"form":form})


def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('next')
    else:
        return  render(request,"Login.html")


def next(request):
    return render(request,"next.html")