from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


def signup_user(request):
    if request.user.is_authenticated:
            return redirect('articles:list')
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    return render(request,'account/signup.html',{'form':form})


def login_user(request):
    if request.user.is_authenticated:
            return redirect('articles:list')
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('articles:list')
    else:
        form=AuthenticationForm()
    return render(request,'account/login.html',{'form':form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')