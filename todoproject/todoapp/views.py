from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todos
from .forms import ListForm

# Create your views here.
def index(request):
    if request.method =="POST":
        form=ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todolist = Todos.objects.all()
            return render(request,'todoapp/index.html',{'todolist':todolist})
    else:
        todolist = Todos.objects.all()
        return render(request,'todoapp/index.html',{'todolist':todolist})

def about(request):
    return render(request,'todoapp/about.html')

def create(request):
    if request.method =="POST":
        form=ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todolist = Todos.objects.all()
            return render(request,'todoapp/create.html',{'todolist':todolist})
    else:
        todolist = Todos.objects.all()
        return render(request,'todoapp/create.html',{'todolist':todolist})


def delete(request,Todoss_id):
    todo=Todos.objects.get(pk=Todoss_id)
    todo.delete()
    return redirect('index')

def yes_finish(request,Todos_id):
    todo=Todos.objects.get(pk=Todos_id)
    todo.finished=False
    todo.save()
    return redirect('index')

def no_finish(request,Todos_id):
    todo=Todos.objects.get(pk=Todos_id)
    todo.finished=True
    todo.save()
    return redirect('index')

def update(request,Todos_id):
    if request.method =="POST":
        todo_list=Todos.objects.get(pk=Todos_id)
        form=ListForm(request.POST or None,instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        todolist = Todos.objects.all()
        return render(request,'todoapp/update.html',{'todolist':todolist})