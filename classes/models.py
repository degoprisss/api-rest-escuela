from django.db import models

from apprentices.models import Apprentices


class Classes(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    students = models.ManyToManyField(Apprentices)

    def __str__(self):
        return self.name
