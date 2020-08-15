from django.shortcuts import render
from django.http import HttpResponse
#from .models import user


def home(request):
     return render(request,'count/base.html')

def num(request):
	 return render(request,'count/num.html')



def about(request):
	 return render(request,'count/about.html')

def counting(request):
    first = int(request.GET['Fnum'])
    last = int(request.GET['Lnum'])
    listnum = []
    if (first < last):
        for i in range(first,last+1):
            listnum.append(i)
        context = {
            'list':listnum,
        }
        return render(request,'count/result.html',context)
    else:
       return HttpResponse('<p> First number should be less than last number </p>')




	
