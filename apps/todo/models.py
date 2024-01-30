from django.db import models


class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    completed = models.BooleanField(
        default=False
    )
    created = models.DateField(
        verbose_name='время',
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title
