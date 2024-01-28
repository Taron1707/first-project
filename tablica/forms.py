from .models import Atricles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AtriclesForm(ModelForm):
    class Meta:
        model = Atricles
        fields = ['title', 'anons', 'textfull', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'anons'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date',
                'type': 'date'
            }),
            'textfull': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'fulltext'
            })
        }

