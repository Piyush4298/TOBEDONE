from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login as LoginUser, logout
from todo_app.forms import TODOForm
from todo_app.models import TODO
from django.contrib.auth import decorators
# Create your views here.

@decorators.login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'todo_app/index.html', context={'form':form, 'todos' : todos})

def login(request):
    if request.method == 'GET':
        form = forms.AuthenticationForm()
        context = {
            'form' : form,
        }
        return render(request, 'todo_app/login.html', context=context)
    elif request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        context = {
            'form' : form,
        }
        if form.is_valid():
            username_ = form.cleaned_data['username']
            password_ = form.cleaned_data['password']
            user = authenticate(username=username_, password=password_)
            print("User Authenticated" ,user)
            if user is not None:
                LoginUser(request, user)
                return redirect('index')
        else:
            return render(request, 'todo_app/login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = forms.UserCreationForm()
        context = {
            "form" : form,
        }
        return render(request, 'todo_app/signup.html', context=context)
    elif request.method == 'POST':
        print(request.POST)
        form = forms.UserCreationForm()
        context = {
            'form' : form,
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'todo_app/signup.html', context=context)

@decorators.login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('index')
        else:
            form = TODOForm()
            return render(request, 'todo_app/index.html', context={'form':form})

def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect('index')

def change_status(request, id, status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('index')

def signout(request):
    logout(request)
    return redirect('login')