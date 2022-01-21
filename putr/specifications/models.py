from django.db import models
from django.contrib.auth.models import User


class Specifications(models.Model):
    version = models.CharField('Версия', max_length=100, unique=True)

    def requirements(self):
        return self.requirements_set.all()

    requirements.short_description = 'Требования'

    date_creation = models.DateTimeField('Дата создания')

    class SpecificationStatuses(models.IntegerChoices):
        AGREED = 1, 'Согласовано'
        NOTAGREED = 2, 'Несогласовано'

    status = models.SmallIntegerField('Статус', choices=SpecificationStatuses.choices, default=SpecificationStatuses.NOTAGREED)
    creator = models.CharField('Создатель', max_length=30)
    exclude = ['creator']

    def __str__(self):
        return f'Спецификация {self.version}'

    def get_absolute_url(self):
        return f'specifications/{self.id}'

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'
        ordering = ['version']
        get_latest_by = 'version'

