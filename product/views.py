from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

def dz(request):
    return render(request, "index.html")

def books(request):
    books = Books.objects.all()
    return render(request, "books.html", {"books": books})
    

def add12(request):
    todo_list = ToDo.objects.all()
    return render(request, "add12.html", {"todo_list": todo_list})


def change12(request):
    return render(request, "change12.html")
    

def deleted12(request):
    return render(request, "deleted12.html")

def add_book(request):
    form= request.POST
    book = Books(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"][:10]
    )
    
    book.save()
    return redirect (Books)
    
