from django import forms
from main.models import ToDoList

class CreateNewList(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)
    
    LIST =  [('Casa', 'Casa'),
        ('Trabalho', 'Trabalho'),
        ('Universidade','Universidade'),
        ('Hobby', 'Hobby'),
        ('Outro', 'Outro'), 
        ]
    
    list_type = forms.ChoiceField(label='Tipo de Lista', choices=LIST)
    #check = forms.BooleanField(required=False)