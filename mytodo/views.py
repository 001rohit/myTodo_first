from django.shortcuts import redirect, render, get_object_or_404
from .models import Todo
def home(request):
    completed_Task = Todo.objects.filter(is_completed=True)
    uncompleted_Task = Todo.objects.filter(is_completed = False)
    context = {
        'completed_Task':completed_Task,
        'uncompleted_Task':uncompleted_Task,
    }
    return render(request,'index.html',context)

def mark_done1(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_undone1(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def addTask(request):
    task = request.POST['task']
    print(task)
    Todo.objects.create(task=task)
    return redirect('home')


def delete_task(request,pk):
    task = get_object_or_404(Todo, pk=pk)
    task.delete()
    return redirect('home')  

def edit_task(request,pk):
    get_task = get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    
    else:
        context = {
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)


