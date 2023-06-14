from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from app.models import Mrsachin ,Family,Sibling,CV
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if request.user is authenticate:
        return redirect('home')
    else:
        if request.method=="GET":
            return render(request,'apphtml/login.html')
        else:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        
@login_required
def home(request):
    mrsachin=Mrsachin.objects.all()
    return render(request,'apphtml/home.html' ,context={'mrsachin':mrsachin})

@login_required
def family(request):
    family=Family.objects.all()
    return render(request,'apphtml/family.html' ,context={'family':family})

@login_required
def sibling(request):
    sibling=Sibling.objects.all()
    return render(request,'apphtml/sibling.html',context={'sibling':sibling} )

@login_required
def cv(request):
    cv=CV.objects.all()
    return render(request,'apphtml/cv.html', context={'cv':cv})


def register(request):
    if request.method=="GET":
        return render(request,'apphtml/register.html')
    else:
        
       
        
        
        email = request.POST['email']
        username = request.POST['username']
        password=request.POST['password']
        User.objects.create_user(username=username,password=password,email=email)
        return redirect('login')

@login_required
   
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')
    
