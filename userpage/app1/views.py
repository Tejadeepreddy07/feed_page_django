from django.shortcuts import render,redirect
from app1.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def isuser(user):
    if(User.objects.filter(username=user).exists()):
        return True
    return False
def userlength(user):
    if(len(user)>8):
        return True
    return False
def userspace(user):
    if(len(user.split())>1):
        return True
    return False
def passlength(passw):
    if(len(passw)>8):
        return True
    return False
def passspecial(passw):
    if(passw.isalnum()):
        return True
    return False

def register(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        pasw=request.POST.get('passw')
        if(isuser(uname)):
            d={'data':'Username is Already exists'}
            return render(request,'register.html',d)
        if(not userlength(uname)):
            d={'data':'username should be greate than 8 letter'}
            return render(request,'register.html',d)
        if(userspace(uname)):
            d={'data':'no space in between then username'}
            return render(request,'register.html',d)
        if(not passlength(pasw)):
            d={'data':'password should be greate than 8 letter'}
            return render(request,'register.html',d)
        if(passspecial(pasw)):
            d={'data':'password should have special '}
            return render(request,'register.html',d)
        #obi=User.objects.create_user(username=user,email=mail,,fpassword=pasw)
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=mail,password=pasw)
        obj.save()
        return render(request,'register.html')
    return render(request,'register.html')

def loginview(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        uname=request.POST.get('uname')
        p=request.POST.get('passw')
        temp=authenticate(request,username=uname,password=p)
        if temp is not None:
            login(request,temp)
            return redirect('profile')
        else:
            d={'data':'enter correct password '}
            return render(request,'login.html',d)
    return render(request,'login.html')

def home(request):
    res=feed.objects.all()[::-1]
    return render(request,'feed.html',{'data':res})

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def post(request):
    if request.method=="POST":
        title=request.POST.get('title')
        ima=request.FILES.get('imae')
        c=request.POST.get('cap')
        uname=request.user.username
        res=feed(person=uname,tile=title,image=ima,caption=c)
        res.save()
        return redirect('home')
    return render(request,'post.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def single(request,n):
    res=feed.objects.get(id=n)
    return render(request,'single.html',{'record':res})

def deleteview(request,n):
    res=feed.objects.get(id=n)
    if(request.user.is_superuser):
        res.delete()
        return redirect('home')
    if(res.person==request.user.username):
        res.delete()
        return redirect('home')
    else:
        d={'data':'invalide user','record':res}
        return render(request,'single.html',d)
def updateview(request,n):
    obj=feed.objects.get(id=n)
    if request.method=="POST":
        t=request.POST.get('title')
        ima=request.FILES.get('imae')
        c=request.POST.get('cap')
        ob=feed.objects.get(id=n)
        if(request.user.is_superuser):
            ob.tile=t
            ob.image=ima
            ob.caption=c
            ob.save()
            return redirect('home')
        if(ob.person==request.user.username):
            ob.tile=t
            ob.image=ima
            ob.caption=c
            ob.save()
            return redirect('home')
        else:
            d={'data':'invalide user','record':obj}
            return render(request,'single.html',d)
    return render(request,'update.html',{'record':obj})