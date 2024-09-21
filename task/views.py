from django.shortcuts import render
from .models import Task
from .forms import TaskForm, UserRegistraionForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, "index.html")

def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "task_list.html", {"tasks":tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user = request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html", {"form": form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user = request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "task_confirm_delete.html", {"task": task})

def register(request):
    if request.method == "POST" :
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserRegistraionForm()
    
    return render(request, "registration/register.html", {"form": form})

@login_required
def change_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        status = request.POST.get('status')
        if status in ['TODO', 'INP', 'DONE']:
            task.status = status
            task.save()
    return redirect('task_list')

