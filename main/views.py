from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
@login_required(login_url='/login')
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+ str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) >=2:
                ls.item_set.create(text = txt, complete = False)
            else:
                print("invalid")
                    
    return render(response, "main/list.html", {"ls": ls})

@login_required(login_url='/login')
def home(response): 
    return render(response, "main/home.html", {})

@login_required(login_url='/login')
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            l = form.cleaned_data["list_type"]
            
            t = ToDoList(name = n, list_type = l)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

@login_required(login_url='/login')
def view(response):
    return render(response, "main/view.html", {})

