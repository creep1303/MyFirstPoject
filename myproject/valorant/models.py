from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.name + '-' + self.role

class Player(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name + '-' + str(self.level)