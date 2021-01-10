from django.db import models
from users.models import CustomUser

# Create your models here.
class rack(models.Model):
    cell_number = models.IntegerField()
    cell_is_empty = models.BooleanField()
    stored_items_count = models.IntegerField()
    stored_items_owner = models.IntegerField()
    stored_since = models.DateTimeField(auto_now=True)
