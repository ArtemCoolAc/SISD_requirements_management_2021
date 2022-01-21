from .models import Releases
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, ModelMultipleChoiceField, \
    SelectMultiple, FloatField

full_block = ['version', 'project', 'specification', 'start_date', 'finish_date', 'description']


class ReleasesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        action = kwargs.pop('action', None)
        self.custom_fields = {'user': user, 'action': action}
        super(ReleasesForm, self).__init__(*args, **kwargs)
        self.call_block(user, action)

    def update_block_form(self, **kwargs):
        user = kwargs.pop('user', None)
        action = kwargs.pop('action', None)
        self.custom_fields = {'user': user, 'action': action}
        self.call_block(user, action)

    def get_custom_fields(self):
        return self.custom_fields

    def call_block(self, user, action):
        if user is not None:
            print(user.groups.all())
            for group in user.groups.all():
                print(dir(group))
                print(group.name)
            groups = list(map(lambda x: x.name, user.groups.all()))
            if 'Архитектор' in groups:
                print('Я тут')
                self.block_fields(full_block)

    def block_fields(self, block_fields):
        for field in block_fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Releases
        exclude = ['creator', 'user']
        widgets = {
            'version': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Версия релиза'
            }),
            'project': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Проект',
                'size': 1}),
            'specification': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Спецификация',
                'size': 1}),
            'start_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время старта'}),
            'finish_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время окончания'}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'}),
        }
