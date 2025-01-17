from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import AddTodoForm

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')


def display_todos(request):
    if not request.user.is_authenticated:
        return redirect('loginuser')

    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign the current user to the task
            todo.save()
            return redirect('mytodos') 
    else:
        form = AddTodoForm()

    todo_list = Todo.objects.filter(user=request.user)

    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/usertodo.html', context)

def delete_todo(request, id):
    if not request.user.is_authenticated:
        return redirect('loginuser')
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('mytodos')

def toggle_status(request, id):
    if not request.user.is_authenticated:
        return redirect('loginuser')
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('mytodos')