from .models import Projects
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, ModelMultipleChoiceField, \
    SelectMultiple, FloatField


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта'
            }),
            'releases': SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Релизы',
                'size': 5}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }

