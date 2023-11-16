from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.description
