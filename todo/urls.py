"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import *
from django.conf import settings
from django.conf.urls.static import static
from product.views import delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add12", add12, name="test1"),
    path("add/todo", add_todo, name="add_todo"),
    path("books", books, name="books"),
    path("book/add", add_book, name="add_book"),
    path("deleted12", deleted12, name="test3"),
    path("change12", change12, name="test2"),
    path( "delete-todo/<id>" , delete_todo, name="delete-todo")
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
