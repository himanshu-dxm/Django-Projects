from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
arr = ['Java','Python','C++','C','DotNet','PHP','JavaScript',
       'Swift','HTML','CSS','SQL','Ruby','Objectice-C',
       'Go','VisualBasic','MATLAB','R','Pearl']
globalcnt = dict()

def index(request):
    mydict = {
        "arr":arr
    }
    return render(request,'indexV.html',context=mydict)

def getquery(request):
    q=request.GET['languages']
    if q in globalcnt:
        globalcnt[q]+=1
    else:
        globalcnt[q]=1
    
    mydict = {
        "q" : q,
        "globalcnt" : globalcnt
    }
    return render(request,'indexV.html',context=mydict)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x : x[1],reverse=True))
    mydict = {
        "arr":arr,
        "globalcnt":globalcnt,
    }
    return render(request,'indexV.html',context=mydict)