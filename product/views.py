from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from product.models import Book

def dz(request):
    return render(request, "index.html")
    
def add12(request):
    todo_list = ToDo.objects.all()
    return render(request, "add12.html", {"todo_list": todo_list})


def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def add_book(request):
    form = request.POST
    book = Book(title=form['title'], subtitle=form['subtitle'])
    book.save()
    return redirect('books')


def change12(request):
    return render(request, "change12.html")
    

def deleted12(request):
    return render(request, "deleted12.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect('test1')
    
def delete_todo(request, id):
    print(id)
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('test1')
