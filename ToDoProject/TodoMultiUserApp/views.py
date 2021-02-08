from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login as loginUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TODOForm
from pip._vendor.requests.api import request
# Create your views here.

def indexM(request):
    form = TODOForm()
    return render(request,'indexM.html',context={'form':form})

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        mydict = {
            "form" : form,
            "errorvalue":False
        }
        return render(request,'login.html',context=mydict)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
                return redirect('indexM')
        else:
            mydict = {
            "form" : form,
            "errorvalue":True
            }
            return render(request,'login.html',context=mydict)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        mydict = {
            "form":form,
            "errorvalue":False
        }
        return render(request,'signup.html',context=mydict)
    else :
        form = UserCreationForm(request.POST)
        mydict = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('indexM')
        else:
            mydict["errorvalue"] = True
            return render(request,'signup.html',context=mydict)

def addtodo(request):
    pass