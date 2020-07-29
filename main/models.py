from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    list_type_choices = models.TextChoices('Casa', 'Trabalho', 'Universidade', 'Hobby', 'Outro')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length = 200)
    list_type = models.CharField(blank=True, choices=list_type_choices, max_length = 100) # OPCIONAL
    finish = models.BooleanField()
    
    def __str__(self):
        return self.name

class Item(models.Model):
    item_priority_choices = models.TextChoices('Alta', 'Media', 'Baixa')
    
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    item_priority = models.CharField(blank=True, choices=item_priority_choices, max_length = 100) # OPCIONAL
    
    
    def __str__(self):
        return self.text