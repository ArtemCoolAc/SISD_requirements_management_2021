from django.db import models


class Projects(models.Model):
    name = models.CharField('Название проекта', max_length=30)
    description = models.TextField('Описание', max_length=250, blank=True, null=True)

    def releases(self):
        return self.releases_set.all()

    releases.short_description = 'Релизы'

    def get_absolute_url(self):
        return f'/projects/{self.id}'


    def __str__(self):
        return f'Проект {self.name}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['id']
        get_latest_by = 'id'
