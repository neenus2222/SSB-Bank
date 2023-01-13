from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Application

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        u_name=request.POST['uname']
        pwd1=request.POST['pass1']
        pwd2=request.POST['pass2']
        if pwd1==pwd2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'Username taken, Try another one')
                return redirect('register')
            else:
                user=User.objects.create_user(username=u_name,password=pwd1)
                user.save();
                messages.info(request,'User Successfully Registered')
                return redirect('login')
                
        else:
            messages.info(request,'Passwords are not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
    return redirect('/')


def login(request):
    if request.method=='POST':
        u_name=request.POST["uname"]
        pwd=request.POST["pwd"]
        user=auth.authenticate(username=u_name,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def appn(request):
    if request.method=="POST":
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=str(request.POST["gender"])
        phno=str(request.POST['phno'])
        district=str(request.POST["district"])
        branch=str(request.POST["branch"])
        account=str(request.POST["account"])
        materials=request.POST.getlist('ch1')
        app1=Application.objects.create(Name=name,DOB=dob,Age=age,Gender=gender,PhNo=phno,District=district,Branch=branch,Account=account,Materials=materials)
        app1.save();
        return redirect('home')
    else:
        return render(request,'application.html')
