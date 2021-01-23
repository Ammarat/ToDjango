from django.shortcuts import render,HttpResponse
from .models import ToDo

def dz(request):
    return render(request, "index.html")

def add12(request):
    todo_list = ToDo.objects.all()
    return render(request, "add12.html", {"todo_list": todo_list})


def change12(request):
    return render(request, "change12.html")
    

def deleted12(request):
    return render(request, "deleted12.html")
