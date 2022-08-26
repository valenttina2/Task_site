from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    date = models.DateField('Дата окончания', max_length=50)