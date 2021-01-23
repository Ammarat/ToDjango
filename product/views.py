from django.shortcuts import render,HttpResponse

def dz(request):
    return render(request, "index.html")

def add12(request):
    return render(request, "add12.html")


def change12(request):
    return render(request, "change12.html")
    

def deleted12(request):
    return render(request, "deleted12.html")
