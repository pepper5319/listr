from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListObject(models.Model):
    name = models.CharField(max_length=255, default="My List")
    owner = models.CharField(max_length=255, null=False)
    static_id = models.CharField(max_length=6, primary_key=True, unique=True, null=False, blank=False)
    owner = models.ForeignKey('auth.User',  # ADD THIS FIELD
        related_name='lists',
        on_delete=models.CASCADE)


    def __str__(self):
        return "{} - {}".format(self.name, self.owner)