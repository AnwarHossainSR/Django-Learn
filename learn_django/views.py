from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    parame = {'name':'Mahedi Hasan'}
    return render (request,'index.html',parame)
def remove(request):
    return HttpResponse('<h1>Remove</h1>')
def capitalize(request):
    return HttpResponse('<h1>Capitalize</h1>')
def newlineremove(request):
    return HttpResponse('<h1>newlineremove</h1>')
def spaceremove(request):
    return HttpResponse('<h1>spaceremove</h1>')
def charcount(request):
    return HttpResponse('<h1>charcount</h1>')