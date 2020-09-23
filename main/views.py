from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages

import requests
import urllib.request


# Create your views here.
@login_required(login_url='/login')
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            if response.POST.get("complete") == "clicked":
                ls.finish = True
                ls.save()
                for i in ls.item_set.all():
                    print(i.complete)
                    i.complete = True
                    print(i.complete)
                    i.save()
                return render(response, "main/list.html", {"ls": ls})

            else:
                ls.finish = False
                ls.save()
                
            for item in ls.item_set.all():
                if response.POST.get("c"+ str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                    
                txt = response.POST.get("t"+ str(item.id))
                date = response.POST.get("d"+ str(item.id))
                #item.deadline_date = date
                item.text = txt
                
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            
            prio = response.POST.get('prio')
            if prio == 'Prioridade':
                prio = 'None'
            
            date = response.POST.get('date')
            if len(txt) >=1:
                ls.item_set.create(text=txt, item_priority=prio, deadline_date=date, complete=False)
            else:
                print("invalid")
        elif response.POST.get("delete"):
            id = response.POST.get('delete')
            ls.item_set.get(id=id).delete()
                    
    return render(response, "main/list.html", {"ls": ls})
    

@login_required(login_url='/login')
def home(response):
    def get_weather(user_in):      
        city = user_in     
        apikey = '83861d949bdda6cba17ddc9f7d095655'
        api_url = 'http://api.openweathermap.org/data/2.5/weather'
        
        params = {'APPID' : apikey, 'q' : city,  'units' : 'metric', 'lang' : 'pt'}
        response = requests.get(api_url, params = params)
        weather = response.json()
        if weather['cod'] == '404':
            return '404'
        
        icon = weather['weather'][0]['icon']
        icon = str('http://openweathermap.org/img/wn/'+icon+'@2x.png')
        
        temp = round(weather['main']['temp'])
        
        w = { 'city':weather['name'], 'country':weather['sys']['country'], 'desc':weather['weather'][0]['description'], 'temp':temp, 'icon':icon }
        print(w)
        return w
    
    id = response.user.id
    ls = ToDoList.objects.filter(user_id=id).all()
    percent = []
    
    for item in ls:
        al = item.item_set.all().count()
        true = item.item_set.filter(complete = 'True').count()
        if true == 0:
            percent.append(str(0)+'%')
        else:
            percent.append(str(round((100*true)/al)) +'%')
            
    
    if response.method == "POST":
        if response.POST.get("weather"):
            city = response.POST.get("city")
            w = get_weather(city)
            if w == '404':
                print(w)
    else:
        loc = requests.get("https://ipinfo.io/").json()
        print(loc['city'])
        w = get_weather(loc['city'])
    
    
    
    return render(response, "main/home.html", {'percent': percent, 'weather': w})

@login_required(login_url='/login')
def create(response):
    form = CreateNewList()
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
        return render(response, "main/create.html", {"form": form})

@login_required(login_url='/login')
def view(response):
    if response.method == "POST":
        if response.POST.get("delete"):
            id = response.POST.get('delete')
            response.user.todolist.get(id=id).delete()
        elif response.POST.get("save"):
            id = response.POST.get("save")
            print(id)
            txt = response.POST.get("t"+ str(id))
            print('txt '+ txt)
            for i in response.user.todolist.all():
                if i.id == int(id):
                    i.name = txt
                    i.save()
            
    return render(response, "main/view.html", {})

