from django import forms

class TareaForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título de la tarea'
        })
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción de la tarea',
            'rows': 4
        })
    )