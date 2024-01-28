from django.db import models


class Atricles(models.Model):
    title = models.CharField('name', max_length=50)
    anons = models.CharField('anons', max_length=250)
    textfull = models.TextField('Text')
    date = models.DateTimeField('datapublikacia')

    def __str__(self):
        return f'new:{self.title}'

    class Meta:
        verbose_name = 'novost'
        verbose_name_plural = 'novosti'
