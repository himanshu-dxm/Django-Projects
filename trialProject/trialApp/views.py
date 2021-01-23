from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *
# Create your views here.

def myfunctioncall(request):
    return HttpResponse('Hello World!!')

def myfunctionabout(request):
    return HttpResponse("About response!")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydict= {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydict)

def firstPage(request):
    return render(request,'index.html')

def secondPage(request):
    return render(request,'second.html')

def thirdPage(request):
    var = "Hello,"
    greeting = "How Are You?"
    fruits = ["apple","mango","banana"]
    mydict = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits
    }
    return render(request,'third.html',context=mydict)

def imagePage(request):
    return render(request,'imagepage.html')

def form(request):
    return render(request,'form.html')

def submitForm(request):
    dict1 = {
        var1 : request.GET['a'],
        
        #var2 :
        
        "method" : request.method
    }
    return JsonResponse(dict1)

def form2(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            #var = str("Form Submitted " + str(request.method))
            #return HttpResponse(var)
            mydict = {
                "form" : form
            }
            mydict["success"] = True
            mydict["successmsg"] = "Form Submitted!"
            return render(request,'form2.html',context=mydict)
            
        else:
            mydictionary = {
                "form" : form
            }
            return render(request,'form2.html',context=mydictionary)
        
    elif request.method=="GET":
        form = FeedbackForm()
        mydict = {
            "form" : form,
        }
        return render(request,'form2.html',context=mydict)
        