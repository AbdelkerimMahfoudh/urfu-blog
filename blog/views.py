from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
def home(request):
    if request.user.is_authenticated:
            return redirect('articles:list')
    # return HttpResponse('Home page')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('About page')
    return render(request,'about.html')
