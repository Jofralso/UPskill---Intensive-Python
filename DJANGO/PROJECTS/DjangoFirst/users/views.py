from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'O seu registo foi efetuado com sucesso!')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})
            
def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('posts')
        
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Olá {username.title()}, bem-vindo de volta!')
                return redirect('posts')
        messages.error(request, 'Username ou Pasword inválidos!')
        return render(redirect,'users/login.html', {'form': form})
    
    
def sign_out(request):
    logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
