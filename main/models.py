from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class ToDoList(models.Model):
    class list_type_choices(models.TextChoices):
        CASA = 'Casa', 'Casa'
        TRABALHO = 'Trabalho', 'Trabalho'
        UNIVERSIDADE = 'Universidade','Universidade'
        HOBBY = 'Hobby', 'Hobby'
        OUTRO = 'Outro', 'Outro' 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length = 200)
    list_type = models.CharField(blank=True, choices=list_type_choices.choices, max_length = 100) # OPCIONAL
    finish = models.BooleanField(default=False)# OPCIONAL
    
    def __str__(self):
        return self.name

class Item(models.Model):
    class item_priority_choices(models.TextChoices):
        ALTA = 'Alta', 'Alta'
        MEDIA = 'Media', 'Media'
        BAIXA = 'Baixa', 'Baixa' 
            
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()# OPCIONAL
    item_priority = models.CharField(blank=True, choices=item_priority_choices.choices, max_length = 100) # OPCIONAL
    deadline_date = models.DateTimeField(blank = True, null=True, default='none') # OPCIONAL
    
    
    def __str__(self):
        return self.text