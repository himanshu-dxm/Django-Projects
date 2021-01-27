from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    
    mydict = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydict)
def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydict = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydict)

def list(request):
    mydict = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydict)

def add(request):
    return render(request,'index.html')

def sortdata(request):
    mydict = {
        "alltodos" : Todo.objects.all().order_by('priority')
    }
    return render(request,'list.html',context=mydict)

def search(request):
    q=request.GET['query']
    mydict = {
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    #return HttpResponse(q)
    return render(request,'list.html',context=mydict)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    
    mydict = {
        "title" : obj.title,
        "descritpion" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydict)

def update(request,id):
    obj= Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    
    obj.save()
    
    mydict = {

        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydict)