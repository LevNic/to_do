from django.db import models
from uuid import uuid4


class User(models.Model):
    """
    To_do service user
    """
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    mail = models.EmailField(unique=True)

    def __str__(self):
        return self.username
