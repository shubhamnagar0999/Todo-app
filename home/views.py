from django.shortcuts import render,redirect
from .models import tasks
# Create your views here.
def home(request):
    alltask = tasks.objects.all()
    return render(request,'home.html',{'tasks':alltask})

def task(request):
    if request.method == "POST":
        task = request.POST['task']
        data = tasks(task=task)
        data.save()
    return redirect("home")

def delete(request,id):
    if request.method == "POST":
        data = tasks.objects.get(id=id)
        data.delete()
        return redirect("home")

def update(request,id):
    data = tasks.objects.get(id=id)
    if request.method == "GET":
        return render(request,'update.html',{"task" : data})

    if request.method == "POST":
        updatedtask = request.POST['updatedtask']
        data.task = updatedtask
        data.save()
        return redirect('home')