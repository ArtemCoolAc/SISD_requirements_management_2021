from django.db import models


class Releases(models.Model):
    version = models.TextField('Версия', max_length=250)
    creator = models.CharField('Создатель', max_length=30)
    project = models.ForeignKey('projects.Projects', verbose_name='Проект',
                                on_delete=models.DO_NOTHING, blank=True, null=True)

    specification = models.OneToOneField('specifications.Specifications', verbose_name='Спецификация',
                                         on_delete=models.DO_NOTHING, blank=True, null=True)

    start_date = models.DateTimeField('Время начала')
    finish_date = models.DateTimeField('Время окончания')
    description = models.TextField('Описание', max_length=250, blank=True, null=True)
    exclude = ['creator']

    def __str__(self):
        return f'Релиз {self.version}'

    def get_absolute_url(self):
        return f'/releases/{self.id}'

    class Meta:
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'
        ordering = ['version']
        get_latest_by = 'version'
