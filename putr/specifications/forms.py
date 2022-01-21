from .models import Specifications
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, ModelMultipleChoiceField, SelectMultiple, FloatField

full_block = ['version']


class SpecificationsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        action = kwargs.pop('action', None)
        self.custom_fields = {'user': user, 'action': action}
        super(SpecificationsForm, self).__init__(*args, **kwargs)
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
            if 'Архитектор' in groups or 'Тестировщик' in groups:
                self.block_fields(full_block)
            if 'Аналитик' in groups:
                self.block_fields(['status'])

    class Meta:
        model = Specifications
        exclude = ['date_creation','creator']
        widgets = {
            'version': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Версия спецификации'
            }),
            'requirements': SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Требования'}),
            'status': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'size': 1
            }),
        }
