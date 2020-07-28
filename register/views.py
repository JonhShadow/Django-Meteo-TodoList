from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def register(response):
    if response.user.is_authenticated:
        messages.info(response, "A sua conta já foi criada.Pode usufruir do Site Super Últil!")
        return render(response, "main/home.html", {})
    else:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
            return redirect("/")     
        else:
            form = RegisterForm()
                
        return render(response, "register/register.html", {"form":form})
    
def login(response):
    if response.user.is_authenticated:
        messages.info(response, "Já efetuou o login.Pode usufruir do Site Super Últil!")
        return render(response, "main/home.html", {})
    else:
        return render(response, "registration/login.html", {})