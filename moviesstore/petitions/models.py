from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    score = models.IntegerField(default=0)
    voters = models.ManyToManyField('auth.User', related_name='petition_votes', blank=True)

    def __str__(self):
        return self.title