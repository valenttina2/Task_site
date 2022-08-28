from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('date')
    return render(request, 'main/index.html',{'title':"Все задачи", 'tasks':tasks,})

def about(request):
    return render(request, 'main/about_us.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма заполнена некорректно"
    form = TaskForm()
    context = {'form':form,
               'error':error}
    return render(request, 'main/create.html', context)
