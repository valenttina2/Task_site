from django.forms import ModelForm, widgets, TextInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields=["title", "task", "date"]
        widgets = {'title': TextInput(attrs={'class':'form-control',
                                             'placeholder':'Введите название'}),
            'task': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Введите описание'}),
            'date': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Введите дату окончания'}),

        }