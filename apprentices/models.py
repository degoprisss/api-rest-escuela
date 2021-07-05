from django.db import models

class Apprentices(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name