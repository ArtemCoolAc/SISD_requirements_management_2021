from .models import Requirements
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, ModelMultipleChoiceField, SelectMultiple

full_block = ['name', 'description', 'type', 'specification', 'linked_requirement', 'link_type']


class RequirementsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        action = kwargs.pop('action', None)
        self.custom_fields = {'user': user, 'action': action}
        super(RequirementsForm, self).__init__(*args, **kwargs)
        self.fields['linked_requirement'].queryset = Requirements.objects.exclude(
            id__exact=self.instance.id)
        self.call_block(user, action)

    def update_block_form(self, **kwargs):
        user = kwargs.pop('user', None)
        action = kwargs.pop('action', None)
        self.custom_fields = {'user': user, 'action': action}
        self.call_block(user, action)

    def get_custom_fields(self):
        return self.custom_fields

    def block_fields(self, block_fields):
        for field in block_fields:
            self.fields[field].widget.attrs['readonly'] = True

    def call_block(self, user, action):
        if user is not None and action == 'update':
            groups = list(map(lambda x: x.name, user.groups.all()))
            if 'Архитектор' in groups:
                self.block_fields(full_block)
            elif 'Руководитель проекта' in groups:
                block_head = full_block + ['executor']
                self.block_fields(block_head)

    class Meta:
        model = Requirements
        exclude = ['date_creation','creator']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название требования',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'status': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'size': 1
            }),
            'type': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип',
                'size': 1
            }),
            'date_creation': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания'
            }),
            'creator': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Создатель'
            }),
            'specification': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Спецификация',
                'size': 1
            }),
            'executor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Исполнитель'
            }),
            # 'linked_requirement': Select(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Связанное требование',
            #     'size': 3
            # }),
            'linked_requirement': SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Тип связи',
            }),
            'link_type': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип связи',
                'size': 1
            })
        }
