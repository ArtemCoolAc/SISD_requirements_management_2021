from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Requirements(models.Model):
    name = models.CharField('Имя', unique=True, max_length=50)
    description = models.TextField('Описание', max_length=250, blank=True, null=True)

    class RequirementStatuses(models.IntegerChoices):
        NEW = 1, 'Новое'
        REJECTED = 2, 'Отвергнуто'
        AGREED = 3, 'Согласовано'
        CANCELED = 4, 'Отменено'
        REALIZED = 5, 'Реализовано'
        UNREALIZED = 6, 'Нереализовано'

    status = models.SmallIntegerField('Статус', choices=RequirementStatuses.choices, default=RequirementStatuses.NEW)

    class RequirementTypes(models.IntegerChoices):
        FUNCTIONAL = 1, 'Функциональное'
        NONFUNCTIONAL = 2, 'Нефункциональное'
        __empty__ = 'Выберите тип требования'

    type = models.SmallIntegerField('Тип требования', choices=RequirementTypes.choices,
                                    default=RequirementTypes.__empty__)

    date_creation = models.DateTimeField('Дата создания')
    creator = models.CharField('Создатель', max_length=30)
    executor = models.CharField('Исполнитель', max_length=30)

    specification = models.ForeignKey('specifications.Specifications', verbose_name='Спецификация',
                                      on_delete=models.DO_NOTHING, blank=True, null=True,
                                      limit_choices_to={'status': 2})

    # linked_requirement = models.OneToOneField('self', verbose_name='Связанные требования', on_delete=models.DO_NOTHING, blank=True, null=True)
    linked_requirement = models.ManyToManyField('self', verbose_name='Связанные требования',
                                                # on_delete=models.DO_NOTHING,
                                                blank=True, null=True)

    class LinkTypes(models.IntegerChoices):
        HIERARCHY = 1, 'Иерархическая'
        DEPENDENCY = 2, 'Зависимость'

    link_type = models.SmallIntegerField('Тип связи', choices=LinkTypes.choices, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/requirements/{self.id}'

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'
        ordering = ['date_creation']
        get_latest_by = 'date_creation'
