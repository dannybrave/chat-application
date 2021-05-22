from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from .decorators import unauthenticated_user


@unauthenticated_user
def sign_up(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            
            return redirect('sign-in')
        else:
            print(form.errors)
            
    context={
        'form':SignUpForm
    }
    return render(request, 'sign-up.html', context)

@unauthenticated_user
def sign_in(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)
            
    context={
        'form':LoginForm
    }
    return render(request,'sign-in.html',context)