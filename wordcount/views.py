from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    countlist = fulltext.split()
    count = len(countlist)
    return render(request,'count.html',{'count':count,'fulltext':fulltext})

def about(request):
    return render(request,'about.html')
