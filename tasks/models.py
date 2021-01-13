from django.db import models
from users.models import CustomUser


# Create your models here.
class TaskStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.RESTRICT)
    creator = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    assigned_to = models.ForeignKey(CustomUser,
        on_delete=models.RESTRICT,
        blank=True,
        related_name= 'assigned'
    )
    tags = models.ManyToManyField(Tag, blank=True)
